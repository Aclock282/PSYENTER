import os

TOKEN = os.getenv("NOTION_TOKEN")

class DB:
    def __init__(self):
        self.TOKEN = TOKEN
        self.ID = "35b59828d4a3805f8629ebd6b7fc14ce"
        pass
