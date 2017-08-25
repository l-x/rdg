from typing import Dict, Any, Union, List
import jinja2

args = Dict[str, Any]
identity = Dict[str, Union[str, int]]
template = jinja2.Template
environment = jinja2.Environment
vocabulary_dict = Dict[str, List[identity]]
