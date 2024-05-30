from typing import Optional, List, Dict, Type
import pandas as pd
from featurify.feature import Feature
from featurify.streamlit.app import streamlit_app
class FeatureStore:
    def __init__(self, name: str, description: str, features: Optional[List[Feature]] = None):
        """
        Initialize a FeatureStore object.

        :param name: Name of the FeatureStore.
        :param description: Description of the FeatureStore.
        :param features: Optional list of Feature objects to initialize the store with.
        """
        self.name = name
        self.description = description
        self.features = {feature.name: feature for feature in features}

    def launch(self):
        """
        Launch the Streamlit app for the FeatureStore.
        """
        streamlit_app(self)

    def get_feature(self, feature_name: str) -> Optional[Feature]:
        """
        Retrieve a feature by name.

        :param feature_name: The name of the feature to retrieve.
        :return: The Feature object if found, else None.
        """
        return self.features.get(feature_name)

    def compute_feature(self, feature_name: str, domain: pd.DataFrame=None) -> pd.DataFrame:
        """
        Compute the given feature for the provided domain DataFrame.

        :param feature: The Feature object to compute.
        :param domain: The domain DataFrame to compute the feature on.
        :return: A DataFrame with the computed feature.
        """
        # Check if the feature has dependencies
        feature = self.get_feature(feature_name)

        if feature.dependencies:
            # Recursively compute dependencies
            dependency_results = {}
            for dep_name in feature.dependencies:
                dependency_results[dep_name] = self.compute_feature(dep_name, domain)
            # Compute the feature using the results of its dependencies
            result = feature.func(*[depdency_df.copy() for depdency_df in dependency_results.values()])
        else:
            # Compute the feature directly if no dependencies
            result = feature.func(domain)
        
        # Ensure the result DataFrame is cast to the appropriate types as defined in the feature's schema
        for col, dtype in feature.schema.items():
            result[col] = result[col].astype(dtype)
        
        return result
