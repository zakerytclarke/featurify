from featurify.feature import Feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_allergies",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type=datetime, sort_key=True),
        Feature(name="end_timestamp", type=datetime),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
    ]
)
def fhir_allergies():
    allergies_df = pd.read_csv("https://zclarke.dev/synthea_medical_dataset/allergies.csv")
    allergies_df["user_id"] =  allergies_df["PATIENT"]
    allergies_df["timestamp"] =  pd.to_datetime(allergies_df["START"])
    allergies_df["end_timestamp"] =  pd.to_datetime(allergies_df["STOP"])
    allergies_df["encounter_id"] =  allergies_df["ENCOUNTER"]
    allergies_df["code"] =  allergies_df["CODE"]
    allergies_df["description"] =  allergies_df["DESCRIPTION"]
   
    return allergies_df

