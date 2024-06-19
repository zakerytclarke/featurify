from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_medications",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="end_timestamp", type="datetime64[ns]"),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/medications.csv")
def fhir_medications(medications_df):
    medications_df["user_id"] =  medications_df["PATIENT"]
    medications_df["timestamp"] =  pd.to_datetime(medications_df["START"])
    medications_df["end_timestamp"] =  pd.to_datetime(medications_df["STOP"])
    medications_df["encounter_id"] =  medications_df["ENCOUNTER"]
    medications_df["code"] =  medications_df["CODE"]
    medications_df["description"] =  medications_df["DESCRIPTION"]
   
    return medications_df




