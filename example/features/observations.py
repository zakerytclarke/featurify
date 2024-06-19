from featurify.feature import Feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_observations",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type=datetime, sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
        Feature(name="value", type=str),
        Feature(name="units", type=str),
    ]
)
def fhir_observations():
    observations_df = pd.read_csv("https://zclarke.dev/synthea_medical_dataset/observations.csv")
    observations_df["user_id"] =  observations_df["PATIENT"]
    observations_df["timestamp"] =  pd.to_datetime(observations_df["DATE"])
    observations_df["encounter_id"] =  observations_df["ENCOUNTER"]
    observations_df["code"] =  observations_df["CODE"]
    observations_df["description"] =  observations_df["DESCRIPTION"]
    observations_df["value"] =  observations_df["VALUE"]
    observations_df["units"] =  observations_df["UNITS"]
   
    return observations_df




