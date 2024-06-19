from featurify.feature import feature, Feature
from featurify.adapter import tsv_feature
import pandas as pd



Merge types:
1. Concat- all dependencies must have the same primary key and sort key field to concatenate, columns will be set to null for any missing features
2. Merge- merge all dependencies
3. Mergeasof- merges all dependencies onto the domain and returns a single dataframe of tha t



@feature(
    name="content_events",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type="datetime64[ns]"),
        Feature(name="content_id", type=str),
        Feature(name="content_activity_type", type=str),
    ]
)
def content_events():

@feature(
    name="content_metadata",
    schema=[
        Feature(name="content_id", type=str, primary_key=True),
        Feature(name="content_type", type=str, sort_key=True),
        Feature(name="content_url", type=str, sort_key=True),
        Feature(name="content_text", type=str, sort_key=True),
    ]
)
def content_metadata():


@feature(
    name="user_demographics",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="gender", type=str),
        Feature(name="age", type=int),
    ]
)
def user_demographics():


@feature(
    name="content_views",
    schema=[
        Feature(name="content_id", type=str, primary_key=True),
        Feature(name="count", type=int),
    ],
    dependencies=["content_events"]
)
def popular_events(df):
    return df[df.content_activity_type=="view"].groupby('content_id').count()

@feature(
    name="popular_events",
    schema=[
        Feature(name="content_id", type=str, primary_key=True),
        Feature(name="count", type=int),
    ],
    dependencies=["content_events"]
)
def popular_events(df):
    return df[df.content_activity_type=="view"].groupby('content_id').count()


@feature(
    name="model_parameters",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="number_recommendations", type=int),
        Feature(name="content_type", type=int),
    ],
)
def model_parameters(df):
    return df[df.content_activity_type=="view"].groupby('content_id').count()


@feature(
    name="content_completed",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="content_id", type=int),
        Feature(name="completed", type=bool),
    ],
)
def content_completed(df):
    return 

@feature(
    name="dataset",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="timestamp", type=str, primary_key=True),
    ]+[Feature(name=f"content_id_{content_id}", type=bool, primary_key=True) for content_id in MODEL.content_ids]
    ,
    dependencies=["content_completed"]
)
def dataset(df):
    return df.groupby('user_id').transpose to content_id as column


MODEL = load_model("model#4")

@feature(
    name="model",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="content_id", type=int),
        Feature(name="score", type=bool),
    ],
    dependencies="dataset"
)
def model(df):
    df['predictions'] = model.predict(df).explode.predicrtion
    Feature(name="user_id", type=str, primary_key=True),

@feature(
    name="merged_predictions",
    schema=[
        Feature(name="user_id", type=str, primary_key=True),
        Feature(name="content_ids", type=List[str]),
    ],
    dependencies=MergeAsOf("model","popular")
)
def sample_content_recommendation_model(df):
    return 