from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_DATABASE = getenv("DB_DATABASE")
DB_HOST = getenv("DB_HOST")
DB_PORT = int(getenv("DB_PORT"))
JWT_KEY = getenv("JWT_KEY")

JWT_ACCESS_LIFETIME = 60*30
JWT_REFRESH_LIFETIME = 60*60*24*7

for key, value in vars().copy().items():
    if key.startswith("__"):
        continue
    if value is None:
        raise ValueError(f"{key} is not defined.")
        
    
