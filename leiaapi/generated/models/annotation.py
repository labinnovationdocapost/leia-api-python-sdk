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
from pydantic import BaseModel, StrictStr
from leiaapi.generated.models.annotation_types import AnnotationTypes

class Annotation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    annotation_type: AnnotationTypes = ...
    application_id: StrictStr = ...
    creation_time: datetime = ...
    document_id: StrictStr = ...
    id: StrictStr = ...
    name: Optional[StrictStr] = None
    prediction: Optional[Dict[str, Any]] = None
    tags: Optional[List[StrictStr]] = None
    __properties = ["annotation_type", "application_id", "creation_time", "document_id", "id", "name", "prediction", "tags"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Annotation:
        """Create an instance of Annotation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Annotation:
        """Create an instance of Annotation from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Annotation.model_validate(obj)

        _obj = Annotation.model_validate({
            "annotation_type": obj.get("annotation_type"),
            "application_id": obj.get("application_id"),
            "creation_time": obj.get("creation_time"),
            "document_id": obj.get("document_id"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "prediction": obj.get("prediction"),
            "tags": obj.get("tags")
        })
        return _obj

