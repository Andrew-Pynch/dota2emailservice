import argparse

from util.util import *


class UserStats(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.current_mmr = self.get_current_mmr()
        self.mmr_history = self.get_mmr_history()
        self.mmr_diff = self.get_mmr_diff()
        self.gpm_average = self.get_gpm_average()

    def __call__(self):
        pass

    def __str__(self):
        return f"""
    Current MMR: {self.current_mmr}
    MMR History: {self.mmr_history}
    Average GPM: {self.gpm_average}
        """

    def get_current_mmr(self):
        return 480

    def get_mmr_history(self):
        return [
            {
                "11-4-2021": 480,
            },
            {
                "11-5-2021": 510,
            },
        ]

    def get_gpm_average(self):
        return 408

    def get_mmr_diff(self):
        return 30
