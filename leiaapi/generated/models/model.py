# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@leia.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr
from leiaapi.generated.models.model_input_types import ModelInputTypes
from leiaapi.generated.models.model_types import ModelTypes
from leiaapi.generated.models.speed import Speed

class Model(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    allow_all_applications: Optional[StrictBool] = None
    allowed_application_ids: Optional[List[StrictStr]] = None
    always_on_workers: Optional[int] = Field(None, description="The number of always on workers to start for this model")
    application_id: Optional[StrictStr] = None
    cores: Optional[StrictFloat] = Field(None, description="The number of CPU cores this model needs to run (If not given will use system defaults)")
    creation_time: datetime = ...
    description: Optional[StrictStr] = None
    documentation: Optional[StrictStr] = None
    id: StrictStr = ...
    input_types: List[ModelInputTypes] = ...
    md5sum: Optional[StrictStr] = Field(None, description="The MD5 sum of the model")
    memory: Optional[StrictFloat] = Field(None, description="The memory in GB this model needs to run (If not given will use system defaults)")
    model_clazz: StrictStr = Field(..., description="The Python class name of the model")
    model_module: StrictStr = Field(..., description="The Python module ghosting the code for the model")
    model_type: ModelTypes = ...
    name: StrictStr = ...
    output_format: Optional[Dict[str, Any]] = None
    short_name: Optional[StrictStr] = None
    size: int = ...
    speed: Optional[Speed] = None
    tags: Optional[List[StrictStr]] = None
    ttl: Optional[int] = Field(None, description="The TTL of the workers hosting this model")
    __properties = ["allow_all_applications", "allowed_application_ids", "always_on_workers", "application_id", "cores", "creation_time", "description", "documentation", "id", "input_types", "md5sum", "memory", "model_clazz", "model_module", "model_type", "name", "output_format", "short_name", "size", "speed", "tags", "ttl"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Model:
        """Create an instance of Model from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model:
        """Create an instance of Model from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Model.parse_obj(obj)

        _obj = Model.parse_obj({
            "allow_all_applications": obj.get("allow_all_applications"),
            "allowed_application_ids": obj.get("allowed_application_ids"),
            "always_on_workers": obj.get("always_on_workers"),
            "application_id": obj.get("application_id"),
            "cores": obj.get("cores"),
            "creation_time": obj.get("creation_time"),
            "description": obj.get("description"),
            "documentation": obj.get("documentation"),
            "id": obj.get("id"),
            "input_types": obj.get("input_types"),
            "md5sum": obj.get("md5sum"),
            "memory": obj.get("memory"),
            "model_clazz": obj.get("model_clazz"),
            "model_module": obj.get("model_module"),
            "model_type": obj.get("model_type"),
            "name": obj.get("name"),
            "output_format": obj.get("output_format"),
            "short_name": obj.get("short_name"),
            "size": obj.get("size"),
            "speed": obj.get("speed"),
            "tags": obj.get("tags"),
            "ttl": obj.get("ttl")
        })
        return _obj

