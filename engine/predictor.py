"""
Prediction Engine
"""

from history_loader import HistoryLoader
from feature import FeatureEngine

class Predictor:

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def run(self):

        history = HistoryLoader(self.csv_path).load()

        feature = FeatureEngine(history)

        df = feature.build()

        print(df.head())

        return df