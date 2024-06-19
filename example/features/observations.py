from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_observations",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
        Feature(name="value", type=str),
        Feature(name="units", type=str),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/observations.csv")
def fhir_observations(observations_df):
    observations_df["user_id"] =  observations_df["PATIENT"]
    observations_df["timestamp"] =  pd.to_datetime(observations_df["DATE"])
    observations_df["encounter_id"] =  observations_df["ENCOUNTER"]
    observations_df["code"] =  observations_df["CODE"]
    observations_df["description"] =  observations_df["DESCRIPTION"]
    observations_df["value"] =  observations_df["VALUE"]
    observations_df["units"] =  observations_df["UNITS"]
   
    return observations_df




