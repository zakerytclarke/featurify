from featurify.feature_store import FeatureStore

from example.feature import external_diabetes_data, diabetes_features, health_target, is_adult, high_blood_pressure, demographics

feature_store = FeatureStore(
    name="Diabetes Model",
    description="Features for Diabetes Model from Sklearn",
    features=[
        external_diabetes_data,
        diabetes_features,
        health_target,
        is_adult,
        high_blood_pressure,
        demographics
    ]
)



feature_store.compute_feature("is_adult")


feature_store.launch()