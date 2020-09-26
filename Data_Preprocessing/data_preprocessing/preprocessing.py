import pandas as pd
import numpy as np
from sklearn import LinearRegression
from sklearn.model_selection import train_test_split

class Preprocessor:

    def __init__(self,file_location):
        self.file_location=file_location

    def preprocess_data(self):
        df=pd.read_csv(file_location)
        df.drop.duplicates(inplace=True)
        return self.encodeCategoricalValues(df)

    # Converting categorical data into numeric values using one hot encoding
    def encodeCategoricalValues(self,data):
        df = pd.get_dummies(data, columns=['sex', 'smoker','region'])

        return df





