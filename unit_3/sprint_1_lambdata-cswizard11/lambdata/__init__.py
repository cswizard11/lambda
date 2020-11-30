import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

def null_count(df):
    return df.isnull().value_counts().sum()

def train_test_split(df, frac):
    X_train, X_test = train_test_split(df, train_size=frac)
    return X_train, X_test
