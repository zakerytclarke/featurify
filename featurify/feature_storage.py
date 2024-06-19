
class FeatureCache:
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


