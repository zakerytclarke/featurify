from featurify.feature_store import FeatureStore
from featurify.feature import feature
import pandas as pd
from sklearn.datasets import load_diabetes



@feature(
    name="health_data",
    schema={
        "user_id": int,
        "age": float,
        "sex": float,
        "bmi": float,
        "bp": float,
        "s1": float,
        "s2": float,
        "s3": float,
        "s4": float,
        "s5": float,
        "s6": float,
    },
    primary_key="user_id"  # Set primary key as user_id
)
def health_data(domain):
    # Load the diabetes dataset as a DataFrame
    diabetes = load_diabetes(as_frame=True)
    df = diabetes['data']
    
    # Create a user_id column from the DataFrame index
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'user_id'}, inplace=True)
    
    return df

# Define the feature using a decorator for health target
@feature(
    name="health_target",
    schema={
        "user_id": int,
        "target": float,
    },
    primary_key="user_id"  # Set primary key as user_id
)
def health_target(domain):
    # Load the diabetes dataset to access the target
    diabetes = load_diabetes(as_frame=True)
    target = diabetes['target']
    
    # Create a DataFrame for the target
    target_df = pd.DataFrame(data={'target': target})
    
    # Create a user_id column from the DataFrame index
    target_df.reset_index(inplace=True)
    target_df.rename(columns={'index': 'user_id'}, inplace=True)
    
    return target_df


@feature(
    name="is_adult",
    schema={
        "user_id": int,
        "is_adult": bool,
    },
    primary_key="user_id",
    dependencies=[
        "health_data"
    ]
)
def is_adult(health_data_df):
    breakpoint()
    health_data_df['is_adult'] = health_data_df.age >=18
    return health_data_df


feature_store = FeatureStore(
    name="Diabetes Model",
    description="Features for Diabetes Model from Sklearn",
    features=[
        health_data,
        health_target,
        is_adult
    ]
)

feature_store.compute_feature("is_adult"),
feature_store.launch()