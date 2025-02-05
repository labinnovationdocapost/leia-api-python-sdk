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



from pydantic import BaseModel, StrictStr, confloat

class Classification(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    accuracy: confloat(le=1, ge=0, strict=True) = ...
    category: StrictStr = ...
    score: confloat(le=1, ge=0, strict=True) = ...
    __properties = ["accuracy", "category", "score"]

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
    def from_json(cls, json_str: str) -> Classification:
        """Create an instance of Classification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Classification:
        """Create an instance of Classification from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Classification.model_validate(obj)

        _obj = Classification.model_validate({
            "accuracy": obj.get("accuracy"),
            "category": obj.get("category"),
            "score": obj.get("score")
        })
        return _obj

