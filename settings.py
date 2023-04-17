from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

mongodb_uri = MONGODB_URI

port= 8000