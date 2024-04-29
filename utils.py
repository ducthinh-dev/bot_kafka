import requests
import os
from dotenv import load_dotenv


class Ninjas:
    def __init__(self):
        load_dotenv()
        self.__KEY = os.environ.get("NINJAS_KEY")
        self.__HEADERS = {
            "X-Api-Key": self.__KEY
        }
        self.__BASE = os.environ.get("NINJAS_BASE")
        pass

    def jokes(self, limit=1):
        endpoint = "v1/jokes"
        response = requests.get(
            self.__BASE+endpoint,
            headers=self.__HEADERS,
            params={"limit": limit})
        return response
