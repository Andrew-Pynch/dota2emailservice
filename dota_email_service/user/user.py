import argparse
import smtplib


from .user_stats import *


class User(object):
    def __init__(self, info):
        self.api_key = None
        self.first_name = info["first_name"]
        self.last_name = info["last_name"]
        self.email = info["email"]
        self.user_id = info["user_id"]
        self.stats: UserStats = UserStats(info["user_id"])

    def __call__(self):
        print(self)

    def __str__(self):
        return f"""
    API Key: {self.api_key}
    First Name: {self.first_name}
    Last Name: {self.last_name}
    Email: {self.email}
    User ID: {self.user_id}
    Stats: {self.stats}
        """

    def set_api_key(self, api_key):
        self.api_key = api_key
