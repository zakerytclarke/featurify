from typing import Union, Literal
class Dependency:
    features: Union[str, Feature]

class MergeDependency:
    features: List[Union[str, Feature]]
    join: Literal["left", "right", "outer"]

class MergeAsOfDependency:
    features: List[Union[str, Feature]]
    join:str #{'left', 'right', 'outer', 'inner'}