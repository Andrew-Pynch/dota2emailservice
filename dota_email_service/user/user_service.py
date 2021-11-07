from typing import List

from util.util import print_symbol_row

from .user import User


def get_users_to_email(api_key) -> List[User]:
    """
    Returns a list of users + api key provided in cli flag
    """
    email_users = [
        User(
            {
                "first_name": "Andrew",
                "last_name": "Pynch",
                "email": "andrewpynchbusiness@gmail.com",
                "user_id": "109856994",
            }
        ),
        User(
            {
                "first_name": "Max",
                "last_name": "Cowan",
                "email": "max.f.cowan@gmail.com",
                "user_id": "11683640",
            }
        ),
    ]
    for user in email_users:
        user.set_api_key(api_key)
        user.set_stats(api_key)
        print(user)

    print_symbol_row()
    return email_users
