from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_claims",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="encounter_id", type=str),
        Feature(name="total", type=int),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/claims.csv")
def fhir_claims(claims_df):
    claims_df["user_id"] =  claims_df["PATIENT"]
    claims_df["timestamp"] =  pd.to_datetime(claims_df["BILLABLEPERIOD"])
    claims_df["encounter_id"] =  claims_df["ENCOUNTER"]
    claims_df["total"] =  claims_df[" TOTAL"]
   
    return claims_df

