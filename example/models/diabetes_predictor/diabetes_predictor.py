from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="diabetes_diagnosis",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
    ],
    dependencies=[MergeAsOfDependency("diabetes_diagnosis", "demographics", "age")]
)
def diabetes_diagnosis(dataset):
    breakpoint()
    dataset
    return dataset

