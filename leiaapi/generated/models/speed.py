# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@leia.io
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Speed(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    VERYFAST = 'VERYFAST'
    FAST = 'FAST'
    SLOW = 'SLOW'
    VERYSLOW = 'VERYSLOW'

