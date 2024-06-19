from featurify.feature import Feature, feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_immunizations",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type=datetime, sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
    ]
)
def fhir_immunizations():
    immunizations_df = pd.read_csv("https://zclarke.dev/synthea_medical_dataset/immunizations.csv")
    immunizations_df["user_id"] =  immunizations_df["PATIENT"]
    immunizations_df["timestamp"] =  pd.to_datetime(immunizations_df["DATE"])
    immunizations_df["encounter_id"] =  immunizations_df["ENCOUNTER"]
    immunizations_df["code"] =  immunizations_df["CODE"]
    immunizations_df["description"] =  immunizations_df["DESCRIPTION"]
   
    return immunizations_df




