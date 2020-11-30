import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split as tts

def null_count(df):
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    X_train, X_test = tts(df, train_size=frac)
    return X_train, X_test
