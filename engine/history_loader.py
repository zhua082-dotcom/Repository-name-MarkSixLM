"""
History Loader
"""

import pandas as pd


class HistoryLoader:

    def __init__(self, path):
        self.path = path

    def load(self):
        """
        读取历史开奖CSV
        """
        df = pd.read_csv(self.path)

        return df

    def latest(self):
        df = self.load()
        return df.tail(1)

    def last_n(self, n):
        df = self.load()
        return df.tail(n)