import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split as tts

class BetterDataFrame(pd.DataFrame):

    def null_count(self):
        return self.isnull().sum().sum()

    def train_test_split(self, frac):
        X_train, X_test = tts(self, train_size=frac)
        return X_train, X_test
