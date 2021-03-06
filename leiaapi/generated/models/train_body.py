# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@leia.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TrainBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'callback_headers': 'object',
        'callback_url': 'str',
        'documents_tag': 'str',
        'execute_after_id': 'str',
        'model_module': 'str',
        'model_name': 'str',
        'model_params': 'object'
    }

    attribute_map = {
        'callback_headers': 'callback_headers',
        'callback_url': 'callback_url',
        'documents_tag': 'documents_tag',
        'execute_after_id': 'execute_after_id',
        'model_module': 'model_module',
        'model_name': 'model_name',
        'model_params': 'model_params'
    }

    def __init__(self, callback_headers=None, callback_url=None, documents_tag=None, execute_after_id=None, model_module=None, model_name=None, model_params=None):  # noqa: E501
        """TrainBody - a model defined in Swagger"""  # noqa: E501
        self._callback_headers = None
        self._callback_url = None
        self._documents_tag = None
        self._execute_after_id = None
        self._model_module = None
        self._model_name = None
        self._model_params = None
        self.discriminator = None
        if callback_headers is not None:
            self.callback_headers = callback_headers
        if callback_url is not None:
            self.callback_url = callback_url
        if documents_tag is not None:
            self.documents_tag = documents_tag
        if execute_after_id is not None:
            self.execute_after_id = execute_after_id
        if model_module is not None:
            self.model_module = model_module
        if model_name is not None:
            self.model_name = model_name
        if model_params is not None:
            self.model_params = model_params

    @property
    def callback_headers(self):
        """Gets the callback_headers of this TrainBody.  # noqa: E501


        :return: The callback_headers of this TrainBody.  # noqa: E501
        :rtype: object
        """
        return self._callback_headers

    @callback_headers.setter
    def callback_headers(self, callback_headers):
        """Sets the callback_headers of this TrainBody.


        :param callback_headers: The callback_headers of this TrainBody.  # noqa: E501
        :type: object
        """

        self._callback_headers = callback_headers

    @property
    def callback_url(self):
        """Gets the callback_url of this TrainBody.  # noqa: E501


        :return: The callback_url of this TrainBody.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this TrainBody.


        :param callback_url: The callback_url of this TrainBody.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def documents_tag(self):
        """Gets the documents_tag of this TrainBody.  # noqa: E501


        :return: The documents_tag of this TrainBody.  # noqa: E501
        :rtype: str
        """
        return self._documents_tag

    @documents_tag.setter
    def documents_tag(self, documents_tag):
        """Sets the documents_tag of this TrainBody.


        :param documents_tag: The documents_tag of this TrainBody.  # noqa: E501
        :type: str
        """

        self._documents_tag = documents_tag

    @property
    def execute_after_id(self):
        """Gets the execute_after_id of this TrainBody.  # noqa: E501


        :return: The execute_after_id of this TrainBody.  # noqa: E501
        :rtype: str
        """
        return self._execute_after_id

    @execute_after_id.setter
    def execute_after_id(self, execute_after_id):
        """Sets the execute_after_id of this TrainBody.


        :param execute_after_id: The execute_after_id of this TrainBody.  # noqa: E501
        :type: str
        """

        self._execute_after_id = execute_after_id

    @property
    def model_module(self):
        """Gets the model_module of this TrainBody.  # noqa: E501


        :return: The model_module of this TrainBody.  # noqa: E501
        :rtype: str
        """
        return self._model_module

    @model_module.setter
    def model_module(self, model_module):
        """Sets the model_module of this TrainBody.


        :param model_module: The model_module of this TrainBody.  # noqa: E501
        :type: str
        """

        self._model_module = model_module

    @property
    def model_name(self):
        """Gets the model_name of this TrainBody.  # noqa: E501


        :return: The model_name of this TrainBody.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this TrainBody.


        :param model_name: The model_name of this TrainBody.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def model_params(self):
        """Gets the model_params of this TrainBody.  # noqa: E501


        :return: The model_params of this TrainBody.  # noqa: E501
        :rtype: object
        """
        return self._model_params

    @model_params.setter
    def model_params(self, model_params):
        """Sets the model_params of this TrainBody.


        :param model_params: The model_params of this TrainBody.  # noqa: E501
        :type: object
        """

        self._model_params = model_params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TrainBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
