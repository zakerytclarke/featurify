from featurify.feature import Feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_procedures",
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
def fhir_procedures():
    procedures_df = pd.read_csv("https://zclarke.dev/synthea_medical_dataset/procedures.csv")
    procedures_df["user_id"] =  procedures_df["PATIENT"]
    procedures_df["timestamp"] =  pd.to_datetime(procedures_df["DATE"])
    procedures_df["encounter_id"] =  procedures_df["ID"]
    procedures_df["code"] =  procedures_df["CODE"]
    procedures_df["description"] =  procedures_df["DESCRIPTION"]
    procedures_df["reason_code"] =  procedures_df["REASONCODE"]
    procedures_df["reason_description"] =  procedures_df["REASONDESCRIPTION"]

    return procedures_df