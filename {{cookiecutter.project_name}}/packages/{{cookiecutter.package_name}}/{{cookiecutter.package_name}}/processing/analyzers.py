import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from typing import List



class AnalyzerUnitTemplate(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]) -> None:
        '''
        Specify variable input as list of strings representing column names of a pd.DataFrame.
        '''
        # YOUR CODE HERE
        return None
    
    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        '''
        Required method for Sklearn TransformerMixin class.
        Remains inactive and performs no action for now.
        Leave as is.
        '''
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series = None):
        '''
        Creates a copy of input dataframe, which is passed to method via the sklearn Pipeline.
        This method performs changes to the dataframe with reference to specified variables.
        The modified copy of the original dataframe is then returned and passed to the next step in pipeline.
        Define your specific transformation here.
        '''
        X = X.copy()
        # YOUR CODE HERE

        return X