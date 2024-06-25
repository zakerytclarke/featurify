from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_conditions",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="end_timestamp", type="datetime64[ns]"),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/conditions.csv")
def fhir_conditions(conditions_df):
    conditions_df["user_id"] =  conditions_df["PATIENT"]
    conditions_df["timestamp"] =  pd.to_datetime(conditions_df["START"])
    conditions_df["end_timestamp"] =  pd.to_datetime(conditions_df["STOP"])
    conditions_df["encounter_id"] =  conditions_df["ENCOUNTER"]
    conditions_df["code"] =  conditions_df["CODE"]
    conditions_df["description"] =  conditions_df["DESCRIPTION"]
   
    return conditions_df


@feature(
    name="fhir_conditions",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="end_timestamp", type="datetime64[ns]"),
        Feature(name="encounter_id", type=str),
        Feature(name="code", type=str),
        Feature(name="description", type=str),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/conditions.csv")
def fhir_conditions(conditions_df):
    conditions_df["user_id"] =  conditions_df["PATIENT"]
    conditions_df["timestamp"] =  pd.to_datetime(conditions_df["START"])
    conditions_df["end_timestamp"] =  pd.to_datetime(conditions_df["STOP"])
    conditions_df["encounter_id"] =  conditions_df["ENCOUNTER"]
    conditions_df["code"] =  conditions_df["CODE"]
    conditions_df["description"] =  conditions_df["DESCRIPTION"]
   
    return conditions_df


@feature(
    name="diabetes_diagnosis",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]", sort_key=True),
        Feature(name="diagnosed_diabetes", type=bool),
    ],
    dependencies=["fhir_conditions"]
)
def diabetes_diagnosis(conditions_df):
    df = conditions_df[conditions_df.description.isin(["Diabetes","Prediabetes"])]
    
    return df

