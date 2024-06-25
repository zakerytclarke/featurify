from featurify.feature_store import FeatureStore

from example.features.allergies import fhir_allergies
from example.features.claims import fhir_claims
from example.features.conditions import fhir_conditions, diabetes_diagnosis
from example.features.encounters import fhir_encounters
from example.features.immunizations import fhir_immunizations
from example.features.medications import fhir_medications
from example.features.observations import fhir_observations
from example.features.patients import fhir_patients, age
from example.features.procedures import fhir_procedures



feature_store = FeatureStore(
    name="FHIR Patient Data",
    description="Features for FHIR ML Models",
    features=[
        fhir_allergies,
        fhir_claims,
        fhir_conditions,
        fhir_encounters,
        fhir_immunizations,
        fhir_medications,
        fhir_observations,
        fhir_patients,
        age,
        fhir_procedures,
        diabetes_diagnosis
    ]
)


feature_store.launch()

