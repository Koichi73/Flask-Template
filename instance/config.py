import os
from dotenv import load_dotenv

load_dotenv() # load environment variables

SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")