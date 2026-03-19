"""
Connection config for NopCommerce (and generic MSSQL) DB.
No dependency on any external settings module; use env vars or pass a dict.
"""
import os
from typing import Any, Optional

# Default ODBC driver name
PYODBC_MSSQL_DRIVER = "ODBC Driver 17 for SQL Server"
PYODBC_MSSQL_CONNECTION_STRING = (
    "DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)


def get_connection_dict_from_env(prefix: str = "NOP_DB") -> dict[str, Any]:
    """
    Build a connection dict from environment variables.
    Variables: {PREFIX}_ENGINE, _SERVER, _NAME, _USERNAME, _PASSWORD, or _DSN.
    """
    engine = os.environ.get(f"{prefix}_ENGINE", "MSSQL").strip()
    server = os.environ.get(f"{prefix}_SERVER", "192.168.253.223").strip()
    database = os.environ.get(f"{prefix}_NAME", "NOPCommerce").strip()
    username = os.environ.get(f"{prefix}_USERNAME", "sa").strip()
    password = os.environ.get(f"{prefix}_PASSWORD", "").strip()
    dsn = os.environ.get(f"{prefix}_DSN", "").strip()

    if dsn:
        return {
            "db_engine": "DSN",
            "db_server": dsn,
            "db_name": "",
            "db_username": "",
            "db_password": "",
        }
    return {
        "db_engine": engine,
        "db_server": server,
        "db_name": database,
        "db_username": username,
        "db_password": password,
    }


def get_connection_string(conn: dict[str, Any], driver: str = PYODBC_MSSQL_DRIVER) -> str:
    """Build pyodbc connection string from connection dict."""
    engine = (conn.get("db_engine") or "MSSQL").strip()
    if engine == "DSN":
        return conn.get("db_server") or ""
    if engine != "MSSQL":
        raise ValueError(f"Unsupported db_engine: {engine}. Only MSSQL and DSN are supported.")
    return PYODBC_MSSQL_CONNECTION_STRING.format(
        driver=driver,
        server=conn.get("db_server", ""),
        database=conn.get("db_name", ""),
        username=conn.get("db_username", ""),
        password=conn.get("db_password", ""),
    )
