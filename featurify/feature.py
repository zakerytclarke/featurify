from typing import Callable, List, Optional, Any
from datetime import timedelta
import pandas as pd

class Feature:
    def __init__(self,
                 name: str,
                 type: Any,
                 primary_key: bool = False,
                 sort_key: bool = False,
                 description: Optional[str] = None):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.sort_key = sort_key
        self.description = description

class FeatureGroup:
    def __init__(self,
                 name: str,
                 func: Callable,
                 schema: List[Feature],
                 dependencies: Optional[List[str]] = None,
                 description: Optional[str] = None,
                 tags: Optional[List[str]] = None,
                 lookback: Optional[timedelta] = None):
        self.name = name
        self.func = func
        self.schema = schema
        self.dependencies = dependencies if dependencies else []
        self.description = description if description else func.__doc__
        self.tags = tags if tags else []
        self.lookback = lookback

def feature(name: str, schema: List[Feature], dependencies: Optional[List[str]] = None,
            description: Optional[str] = None, tags: Optional[List[str]] = None,
            lookback: Optional[timedelta] = None):
    def decorator(func: Callable):
        feature_instance = FeatureGroup(
            name=name,
            func=func,
            schema=schema,
            dependencies=dependencies,
            description=description,
            tags=tags,
            lookback=lookback
        )
        def wrapper(*args, **kwargs):
            return feature_instance.func(*args, **kwargs)
        wrapper.feature = feature_instance
        return wrapper
    return decorator
