import os

class DB:
    def __init__(self):
        self.TOKEN = str(os.getenv("NOTION_TOKEN"))
        self.ID = "35b59828d4a3805f8629ebd6b7fc14ce"
        pass
