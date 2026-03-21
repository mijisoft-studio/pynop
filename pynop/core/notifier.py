import smtplib
import settings
from datetime import datetime
import pymsteams
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Notify:
    def __init__(self, name):
        """
        Initialize Notifier，support multiple notification tools.
        :param name: notifier name
        """
        self.name = name
        self.notifiers = self._initialize_notifiers()

    def _initialize_notifiers(self):
        # Automatically initializes all available notification tools.
        return [
            SlackNotify(self.name),
            EmailNotify(self.name),
        ]

    def notify(self, subject, content):
        # Call the notification method of all notification tools.
        for notifier in self.notifiers:
            try:
                if hasattr(notifier, "notify"):
                    notifier.notify(subject, content)
            except Exception as e:
                print(f"Error in {notifier.__class__.__name__} notification: {e}")

    def notify_started(self):
        self.notify("Started", "Batch task started successfully.")

    def notify_exited(self):
        self.notify("Exited", "Batch task exited successfully.")

    def notify_error(self, tb):
        self.notify("Has some error", "Error details are below:\n" + tb)

    def notify_report(self, report_dict):
        content = ""
        for report_name, report_content in report_dict.items():
            content += f"{report_name}: {str(report_content)}\n"
        self.notify("Biz Reports", content.strip())

    def close(self):
        # Close all notification tool connections.
        for notifier in self.notifiers:
            try:
                if hasattr(notifier, "close"):
                    notifier.close()
            except Exception as e:
                print(f"Error closing {notifier.__class__.__name__} notifier: {e}")


class SlackNotify:
    def __init__(self, name):
        self.name = name
        try:
            self.channel_id = settings.SLACK_CHANNEL_ID
            if hasattr(settings, "SLACK_BOT_TOKEN") and settings.SLACK_BOT_TOKEN:
                self.client = WebClient(token=settings.SLACK_BOT_TOKEN)
            else:
                self.client = None
            print("slack setting ******")
            print(self.channel_id, settings.SLACK_BOT_TOKEN)
        except Exception as e:
            print(f"Error instantiates Slack client: {e}")
            self.client = None  # Make sure server is None for subsequent checks

    def now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def notify(self, subject, content):
        if self.client is None:
            print("Slack client is not initialized.")
            return
        try:
            result = self.client.chat_postMessage(
                channel=self.channel_id,
                text="*[{name}]* ({time}) {subject}\n{content}".format(
                    name=self.name, time=self.now(), subject=subject, content=content
                ),
            )
            if not result["ok"]:
                print(result)

        except SlackApiError as e:
            print(f"Failed to send Slack message: {e}")


class EmailNotify:
    def __init__(self, name):
        self.name = name
        self.server = None  # Initializing the SMTP connection
        try:
            # connect to SMTP server
            self.sender_email = settings.SENDER_EMAIL
            self.receiver_email = settings.RECEIVER_EMAIL.split(",")
            self.email_server_addr = settings.EMAIL_SERVER_ADDR
            self.email_server_port = settings.EMAIL_SERVER_PORT

            if self.email_server_addr and self.email_server_port and self.sender_email:
                self.server = smtplib.SMTP(self.email_server_addr, self.email_server_port)
        except Exception as e:
            print(f"Error initializing SMTP connection: {e}")
            self.server = None  # Make sure server is None for subsequent checks

    def now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def notify(self, subject, content):
        # Ban Success Mail
        if subject != "Has some error":
            return
        if self.server is None:
            print("SMTP server is not initialized.")
            return

        # Creat message object
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = ", ".join(self.receiver_email)
        message["Subject"] = "[{name}]{subject}".format(name=self.name, subject=subject)

        # email text
        msg = """
<!DOCTYPE html>
<html>
<body>
    <p><b>[{name}]({time}) {subject}</b></p>
    <p>{content}</p>
</body>
</html>
""".format(name=self.name, time=self.now(), subject=subject, content=content)
        message.attach(MIMEText(msg, "html"))

        try:
            if self.sender_email and self.receiver_email:
                # send email
                self.server.sendmail(self.sender_email, self.receiver_email, message.as_string())
        except Exception as e:
            print(f"Failed to send email: {e}")

    def close(self):
        # Closing the SMTP Connection
        if self.server is not None:
            try:
                self.server.quit()
            except Exception as e:
                print(f"Error closing SMTP connection: {e}")

