from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
API_PUBLISHABLE_KEY = os.getenv("API_PUBLISHABLE_KEY")