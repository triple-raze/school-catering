from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER      = getenv("DB_USER")
    DB_PASSWORD  = getenv("DB_PASSWORD")
    DB_DATABASE  = getenv("DB_DATABASE")
    DB_HOST      = getenv("DB_HOST")
    DB_PORT      = int(getenv("DB_PORT"))

    for field in [DB_USER, DB_DATABASE, DB_HOST, DB_PORT]:
        if not field:
            raise ValueError(f"{field} is not defined")
