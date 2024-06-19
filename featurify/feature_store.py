from typing import Optional, List, Callable
import pandas as pd
from featurify.feature import FeatureGroup  # assuming this is the path to your refactored Feature class
from featurify.streamlit.app import streamlit_app  # assuming this is the path to your Streamlit app

class ComputeSettings:
    mode: str = "offline"
    read_from_cache: bool = True
    write_to_cache: bool = True
    online_store: str
    offline_store: str

class FeatureStore:
    def __init__(self, name: str, description: str, features: Optional[List[Callable]] = None):
        """
        Initializes a new Feature Store with a given name and description.

        Args:
            name (str): The name of the feature store.
            description (str): A brief description of what the feature store contains or represents.
            features (Optional[List[Callable]]): A list of decorated feature functions which are converted into Feature objects.
        """
        self.name = name
        self.description = description
        self.features = {f.feature.name: f.feature for f in features} if features else {}
        # self.feature_storage = 
        # self.merge_settings = 

    def get_feature_group(self, feature_name: str) -> Optional[FeatureGroup]:
        """
        Retrieve a feature by name from the store.

        Args:
            feature_name (str): The name of the feature to retrieve.

        Returns:
            Feature: The feature object if found, else None.
        """
        return self.features.get(feature_name)

    def define_feature_group(self, feature:FeatureGroup, overwrite=False):
        self.features[feature_name]


    def test_feature_store(self):
        # Ensure that all depedencies are accounted for

        # Ensure that all of the types match up 

        # Ensure that there are not features with
        pass

    def compute_feature_group(self, feature_name: str, domain: pd.DataFrame = None) -> pd.DataFrame:
        """
        Compute the specified feature group using its definition and any necessary dependencies.

        Args:
            feature_name (str): The name of the feature to compute.
            domain (pd.DataFrame): A DataFrame representing the domain data on which the feature should be computed.

        Returns:
            pd.DataFrame: A DataFrame containing only the columns specified in the feature's schema.
        """
        feature = self.get_feature_group(feature_name)
        if not feature:
            raise ValueError(f"Feature {feature_name} not found in the feature store.")

        if feature.dependencies:
            dependency_data_frames = {dep: self.compute_feature(dep, domain) for dep in feature.dependencies}
            args = [dependency_data_frames[dep] for dep in feature.dependencies]
            result = feature.func(*args)
        else:
            result = feature.func(domain)

        # Restrict the output to only include columns specified in the schema
        output_df = pd.DataFrame()
        for ft in feature.schema:
            if ft.name in result.columns:
                output_df[ft.name] = result[ft.name].astype(ft.type)
            else:
                raise ValueError(f"Column {ft.name} expected by schema but not produced by feature {feature_name}.")

        return output_df

    def launch(self):
        """
        Launches a Streamlit app configured to use this Feature Store.
        """
        streamlit_app(self)
