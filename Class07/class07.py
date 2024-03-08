from typing import Dict, Union, Optional
import pprint

Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data: Dict[Key, Value]= {
                        "fname": "Abdul Qadir",
                       "name": "Muhammad Saqlain",
                       "eduction": "M.A Economics"
                       }
pprint.pprint(data)