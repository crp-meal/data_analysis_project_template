from sklearn.pipeline import Pipeline

from processing import preprocessors as pp
from processing import analyzers as analyze

### DATA PREPROCESSING
preprocessing_pipeline = Pipeline(
    [
        (
            "Preprocessing pipeline step One",
            pp.ColumnLabelNormalizer()
        ),
        (
            "Preprocessing pipeline Step Two",
            print("Preprocessing step two")
        )
    ]
)


### DATA FILTERING AND VARIABLE SELECTION
filtering_pipeline = Pipeline(
    [
        (
            "Filtering pipeline step One",
            print('Step one')
        ),
        (
            "Filtering pipeline Step Two",
            print('Step two')
        )
    ]
)