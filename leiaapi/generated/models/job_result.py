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
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from leiaapi.generated.models.classification import Classification
from leiaapi.generated.models.document import Document
from typing import Any, List
from pydantic import StrictStr, Field

JOBRESULT_ONE_OF_SCHEMAS = ["Classification", "Document", "List[Document]", "object"]

class JobResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: Document
    oneof_schema_1_validator: Optional[Document] = None
    # data type: List[Document]
    oneof_schema_2_validator: Optional[List[Document]] = None
    # data type: Classification
    oneof_schema_3_validator: Optional[Classification] = None
    # data type: object
    oneof_schema_4_validator: Optional[Any] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(JOBRESULT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: Document
        if type(v) is not Document:
            error_messages.append(f"Error! Input type `{type(v)}` is not `Document`")
        else:
            match += 1

        # validate data type: List[Document]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # validate data type: Classification
        if type(v) is not Classification:
            error_messages.append(f"Error! Input type `{type(v)}` is not `Classification`")
        else:
            match += 1

        if match == 0:
            # validate data type: object
            try:
                instance.oneof_schema_4_validator = v
                match += 1
            except ValidationError as e:
                error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into JobResult with oneOf schemas: Classification, Document, List[Document], object. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into JobResult with oneOf schemas: Classification, Document, List[Document], object. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> JobResult:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> JobResult:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into Document
        try:
            instance.actual_instance = Document.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into List[Document]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into Classification
        try:
            instance.actual_instance = Classification.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match == 0:
            # deserialize data into object
            try:
                # validation
                instance.oneof_schema_4_validator = json.loads(json_str)
                # assign value to actual_instance
                instance.actual_instance = instance.oneof_schema_4_validator
                match += 1
            except ValidationError as e:
                error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into JobResult with oneOf schemas: Classification, Document, List[Document], object. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into JobResult with oneOf schemas: Classification, Document, List[Document], object. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
