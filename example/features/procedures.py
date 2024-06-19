from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_procedures",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
        Feature(name="reason_code", type=str),
        Feature(name="reason_description", type=str),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/procedures.csv")
def fhir_procedures(procedures_df):
    procedures_df["user_id"] =  procedures_df["PATIENT"]
    procedures_df["timestamp"] =  pd.to_datetime(procedures_df["DATE"])
    procedures_df["encounter_id"] =  procedures_df["ID"]
    procedures_df["code"] =  procedures_df["CODE"]
    procedures_df["description"] =  procedures_df["DESCRIPTION"]
    procedures_df["reason_code"] =  procedures_df["REASONCODE"]
    procedures_df["reason_description"] =  procedures_df["REASONDESCRIPTION"]

    return procedures_df