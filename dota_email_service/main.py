import argparse
import smtplib
import ssl

from email_service.email_service import EmailConfig, send_user_stats_email
from user.user_service import get_users_to_email
from util.util import *


class DotaStatsEmailService(object):
    def __init__(self, info):
        print_symbol_row("=")
        print("DOTA 2 STATS EMAIL SERVICE")
        print_symbol_row("=")
        self.api_key = info.api_key

        self.email_users = get_users_to_email(self.api_key)

        self.email_config = EmailConfig(info.password)

        # Create a secure SSL context
        self.context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL(
            self.email_config.smtp_server, self.email_config.port, context=self.context
        )
        self.server.login(self.email_config.sender_email, self.email_config.password)

    def __call__(self):
        for user in self.email_users:
            send_user_stats_email(user, self.server, self.email_config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="dota 2 stats emailer service")

    parser.add_argument("-a", "--a", dest="api_key", help="api key", required=True)

    parser.add_argument(
        "-p", "--p", dest="password", help="email password", required=True
    )

    args = parser.parse_args()

DotaStatsEmailService(args)()
