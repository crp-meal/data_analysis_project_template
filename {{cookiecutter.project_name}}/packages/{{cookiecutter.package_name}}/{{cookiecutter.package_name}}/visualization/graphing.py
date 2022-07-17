from {{cookiecutter.package_name}}.config import config

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

import plotly.graph_objs as go
import pandas as pd

from typing import List


########### GRAPH LAYOUTS ##############

# Consider moving this somewhere else?

def generate_standard_graph_layout(title=None, show_legend=False):
    layout = go.Layout(
        template = 'plotly_white',
        autosize = False,
        bargap = 0.25,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        width = 330*2,
        height = 200*2,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        showlegend = show_legend,
        title={
            'text': title,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 18
        }},


        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': False,
            'range': [0, 100],
            'showgrid': True,
            'showline': True,
            'title': 'Response rate (%)',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
        }
    )
    
    return layout



############# Grapher ##################

class Grapher:
    def __init__(self):
        return self
        
    def GroupedBarChart(dataframe, variable, group_variable=None, title=None, legend=False, export=False):
        COLORS = ['#E54893', '#84AE40', '#000000']
        data = []

        if group_variable!=None:
            legend = True
            for group in list(dataframe[group_variable].unique()):
                data.append(
                    go.Bar(
                        x = dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).sort_index().index,
                        y = (dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).sort_index().values)*100,

                        marker = {
                            'color': COLORS[group],
                            'line': {
                                'color': 'rgb(255, 255, 255)',
                                'width': 2}
                        },
                        name = f"{group_variable} = {group}"
                    )
                )
        else: 
            legend = True
            data = go.Bar(
                        x = dataframe[variable].value_counts(normalize=True).sort_index().index,
                        y = (dataframe[variable].value_counts(normalize=True).sort_index().values)*100,

                        marker = {
                            'color': COLORS[0],
                            'line': {
                                'color': 'rgb(255, 255, 255)',
                                'width': 2}
                        }
                    )

        figure = go.Figure(data=data, layout=generate_standard_graph_layout(title=title, show_legend=legend))

        if export==True:
            figure.write_image(f"{config.OUTPUT_DIR}/graphical_output/{variable}_by_{group_variable}.png", scale=2)

        return figure


##### VISUALIZATION CLASS FOR PIPELINE ###########
### MOVE SOMEPLACE ELSE ###

class ProduceGraphsPrototype(BaseEstimator, TransformerMixin):
    def __init__(self, dependent_variable: str, independent_variables: List[str]):
        ''' Extracts selected variables only. '''

        if not isinstance(independent_variables, list):
            raise ValueError("variables must be given as elements of list.")
        
        self.dependent_variable = dependent_variable
        self.independent_variables = independent_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        
        X = X.copy()
        for variable in self.independent_variables:
            Grapher.GroupedBarChart(X, self.dependent_variable, group_variable=variable, title='target', legend=True, export=True)

        return X