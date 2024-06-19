from featurify.feature import feature, Feature
from featurify.adapter import tsv_feature
import pandas as pd




@feature(
    name="external_diabetes_data",
    schema=[
        Feature(name="AGE", type=int),
        Feature(name="SEX",type=int),
        Feature(name="BMI", type=float),
        Feature(name="BP", type=float),
        Feature(name="S1", type=float),
        Feature(name="S2", type=float),
        Feature(name="S3", type=float),
        Feature(name="S4", type=float),
        Feature(name="S5", type=float),
        Feature(name="S6", type=float),
        Feature(name="Y", type=float),
    ]
)
@tsv_feature("https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt")
def external_diabetes_data(domain):
    pass


@feature(
    name="diabetes_features",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="age", type=int),
        Feature(name="sex", type=float),
        Feature(name="bmi", type=float),
        Feature(name="bp", type=float),
        Feature(name="s1", type=float),
        Feature(name="s2", type=float),
        Feature(name="s3", type=float),
        Feature(name="s4", type=float),
        Feature(name="s5", type=float),
        Feature(name="s6", type=float)
    ],
    dependencies=["external_diabetes_data"]
)
def diabetes_features(external_diabetes_data_df):
    external_diabetes_data_df['user_id'] = external_diabetes_data_df.index
    return external_diabetes_data_df.rename(columns={"AGE": "age", "SEX": "sex", "BMI": "bmi", "BP": "bp", "S1": "s1", "S2": "s2", "S3": "s3", "S4": "s4", "S5": "s5", "S6": "s6"})

@feature(
    name="health_target",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="target", type=float)
    ],
    dependencies=["external_diabetes_data"]
)
def health_target(external_diabetes_data_df):
    external_diabetes_data_df['user_id'] = external_diabetes_data_df.index
    external_diabetes_data_df['target'] = external_diabetes_data_df['Y']
    return external_diabetes_data_df

@feature(
    name="demographics",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="age", type=int),
        Feature(name="sex", type=str)
    ],
    dependencies=["diabetes_features"]
)
def demographics(health_data_df):
    health_data_df['sex'] = health_data_df.sex.apply(lambda sex: "Male" if sex == 1 else "Female")
    return health_data_df

@feature(
    name="is_adult",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="is_adult", type=bool)
    ],
    dependencies=["diabetes_features"]
)
def is_adult(health_data_df):
    health_data_df['is_adult'] = health_data_df.age >= 18
    return health_data_df

@feature(
    name="high_blood_pressure",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="high_blood_pressure", type=bool)
    ],
    dependencies=["diabetes_features"]
)
def high_blood_pressure(health_data_df):
    health_data_df['high_blood_pressure'] = health_data_df.bp >= 120
    return health_data_df

@feature(
    name="model_features",
    schema=[
        Feature(name="user_id", type=str,primary_key=True),
        Feature(name="age", type=int)
    ],
    dependencies=MergeDependecy(features=["demographics", "health_data"]),
    merge_dependencies=True
)
def model_features(merged_features_df):
    return merged_features_df

@feature(
    name="model",
    schema=[
        Feature(name="user_id", type=str,primary_key=True),
        Feature(name="age", type=int)
    ],
    dependencies=["model_features"],
    merge_dependencies=True
)
def model_features(merged_features_df):
    return merged_features_df

@feature(
    name="at_risk",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="at_risk", type=bool)
    ],
    dependencies=["model_features"],
    merge_dependencies=True
)
def model_features(merged_features_df):
    return merged_features_df

