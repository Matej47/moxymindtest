import os
import requests
from dotenv import load_dotenv

# Load the .env file at the very start
load_dotenv()

class ReqresClient:
    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        # Headers need to be set after loading the env
        self.HEADERS = {
            "x-api-key": os.getenv("REQRES_API_KEY"),
            "User-Agent": "python-requests/3.x"
        }

    def get_users(self, page=1):
        return requests.get(
            f"{self.BASE_URL}/users",
            params={"page": page},
            headers=self.HEADERS
        )

    def create_user(self, payload):
        return requests.post(
            f"{self.BASE_URL}/users",
            json=payload,
            headers=self.HEADERS
        )
