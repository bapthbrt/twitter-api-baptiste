# app/models.py
import datetime


class Tweet:
    def __init__(self, text):
        self.text = text
        self.created_at = datetime.datetime.now()
        self.id = None
