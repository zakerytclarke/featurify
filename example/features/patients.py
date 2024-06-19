from featurify.feature import Feature, feature
from featurify.adapter import csv_feature
from datetime import datetime
import pandas as pd

@feature(
    name="fhir_patients",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="date_of_birth", type="datetime64[ns]"),
        Feature(name="date_of_death", type="datetime64[ns]"),
        Feature(name="first_name", type=str),
        Feature(name="last_name", type=str),
        Feature(name="married", type=bool),  
        Feature(name="race", type=str),   
        Feature(name="ethnicity", type=str),  
        Feature(name="gender", type=str),     
        Feature(name="address", type=str),  
        Feature(name="birthplace", type=str),     
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/patients.csv")
def fhir_patients(patients_df):
    patients_df["user_id"] =  patients_df["patient"]
    patients_df["date_of_birth"] =  pd.to_datetime(patients_df["birthdate"])
    patients_df["date_of_death"] =  pd.to_datetime(patients_df["deathdate"])

    patients_df["first_name"] = patients_df["first"]
    patients_df["last_name"] = patients_df["last"]
    patients_df["married"] = patients_df["marital"].map({'M': True, 'S': False})
   
    return patients_df


@feature(
    name="age",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="age", type=int),
    ]
)
@csv_feature("https://zclarke.dev/synthea_medical_dataset/patients.csv")
def fhir_patients(patients_df):
    patients_df["user_id"] =  patients_df["patient"]
    patients_df["date_of_birth"] =  pd.to_datetime(patients_df["birthdate"])
    patients_df["date_of_death"] =  pd.to_datetime(patients_df["deathdate"])

    patients_df["first_name"] = patients_df["first"]
    patients_df["last_name"] = patients_df["last"]
    patients_df["married"] = patients_df["marital"].map({'M': True, 'S': False})
   
    return patients_df