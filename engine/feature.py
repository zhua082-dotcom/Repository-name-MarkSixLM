"""
MarkSixLM Feature Engine
"""
import pandas as pd
import numpy as np
class FeatureEngine:

    def __init__(self, history):
        self.history = history.copy()

    def build(self):

        df = self.history.copy()

        features = []

        for number in range(1,50):

            appear = (df.values == number).any(axis=1).astype(int)

            freq10 = pd.Series(appear).rolling(10,min_periods=1).sum()

            freq30 = pd.Series(appear).rolling(30,min_periods=1).sum()

            gap = []

            last = -1

            for i,v in enumerate(appear):

                if v==1:

                    gap.append(0)

                    last=i

                else:

                    if last==-1:

                        gap.append(i+1)

                    else:

                        gap.append(i-last)

            feature = {

                "number":number,

                "freq10":freq10.iloc[-1],

                "freq30":freq30.iloc[-1],

                "gap":gap[-1]

            }

            features.append(feature)

        return pd.DataFrame(features)
