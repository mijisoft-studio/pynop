import os
import environ
from pathlib import Path

print ("============================== Sync Settings ==============================")

env = environ.Env()

BASE_DIR = Path(__file__).parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


print ("============================== Sync Settings ==============================")
