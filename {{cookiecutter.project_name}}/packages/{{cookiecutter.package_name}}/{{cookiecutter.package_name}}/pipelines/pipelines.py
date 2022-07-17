from sklearn.pipeline import Pipeline

from processing import preprocessors as pp
from processing import analyzers as analyze
from visualization import graphing

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


### OUTPUT GENERATION PIPELINE
output_pipeline = Pipeline(
    [
        (
            "Output pipeline step One",
            graphing.ProduceGraphsPrototype('target', ['v18q', 'v14a'])
        ),
        (
            "Output pipeline Step Two",
            print('Step two')
        )
    ]
)