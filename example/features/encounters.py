from featurify.feature import Feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_encounters",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type=datetime, sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
        Feature(name="reason_code", type=str),
        Feature(name="reason_description", type=str),
    ]
)
def fhir_encounters():
    encounters_df = pd.read_csv("https://zclarke.dev/synthea_medical_dataset/encounters.csv")
    encounters_df["user_id"] =  encounters_df["PATIENT"]
    encounters_df["timestamp"] =  pd.to_datetime(encounters_df["DATE"])
    encounters_df["encounter_id"] =  encounters_df["ID"]
    encounters_df["code"] =  encounters_df["CODE"]
    encounters_df["description"] =  encounters_df["DESCRIPTION"]
    encounters_df["reason_code"] =  encounters_df["REASONCODE"]
    encounters_df["reason_description"] =  encounters_df["REASONDESCRIPTION"]

    return encounters_df


