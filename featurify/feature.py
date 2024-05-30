from typing import Callable, List, Optional, Dict, Any
from datetime import timedelta
from functools import wraps

class Feature:
    def __init__(self,
                 name: str,
                 description: Optional[str],
                 func: Callable,
                 schema: Dict[str, Any],
                 primary_key: str,
                 sort_key: Optional[str] = None,
                 tolerance: Optional[float] = None,
                 tags: Optional[List[str]] = None,
                 dependencies: Optional[List[str]] = None,
                 lookback: Optional[timedelta] = None):
        """
        Initialize a Feature object.

        :param name: Name of the feature.
        :param description: Description of the feature.
        :param func: Function to compute the feature.
        :param schema: Schema dictionary mapping column names to pandas data types.
        :param primary_key: Primary key for the feature.
        :param sort_key: Optional sort key for the feature.
        :param tolerance: Optional tolerance value for the feature.
        :param tags: Optional list of tags associated with the feature.
        :param dependencies: Optional list of feature names this feature depends on.
        :param lookback: Optional lookback period as a timedelta.
        """
        self.name = name
        self.description = description if description else func.__doc__
        self.func = func
        self.schema = schema
        self.primary_key = primary_key
        self.sort_key = sort_key
        self.tolerance = tolerance
        self.tags = tags if tags else []
        self.dependencies = dependencies if dependencies else []
        self.lookback = lookback

    def add_dependency(self, feature_name: str):
        """
        Add a dependency to the feature.

        :param feature_name: Name of the feature to add as a dependency.
        """
        if feature_name not in self.dependencies:
            self.dependencies.append(feature_name)

    def __repr__(self):
        """
        String representation of the Feature object.
        """
        return (f"Feature(name={self.name}, description={self.description}, schema={self.schema}, "
                f"primary_key={self.primary_key}, sort_key={self.sort_key}, tolerance={self.tolerance}, "
                f"tags={self.tags}, dependencies={self.dependencies}, lookback={self.lookback})")

def feature(
        name: str,
        schema: Dict[str, Any],
        primary_key: str,
        description: Optional[str] = None,
        sort_key: Optional[str] = None,
        tolerance: Optional[float] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[str]] = None,
        lookback: Optional[timedelta] = None
    ):
    def decorator(func: Callable):
        return Feature(
            name=name,
            description=description if description else func.__doc__,
            func=func,
            schema=schema,
            primary_key=primary_key,
            sort_key=sort_key,
            tolerance=tolerance,
            tags=tags,
            dependencies=dependencies,
            lookback=lookback
        )
    return decorator