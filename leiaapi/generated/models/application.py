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

class Application(object):
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
        'api_key': 'str',
        'application_name': 'str',
        'application_type': 'ApplicationTypes',
        'creation_time': 'datetime',
        'dedicated_workers': 'bool',
        'dedicated_workers_max_models': 'int',
        'dedicated_workers_ttl': 'int',
        'default_job_callback_url': 'str',
        'email': 'str',
        'first_name': 'str',
        'id': 'str',
        'job_counts': 'object',
        'last_name': 'str'
    }

    attribute_map = {
        'api_key': 'api_key',
        'application_name': 'application_name',
        'application_type': 'application_type',
        'creation_time': 'creation_time',
        'dedicated_workers': 'dedicated_workers',
        'dedicated_workers_max_models': 'dedicated_workers_max_models',
        'dedicated_workers_ttl': 'dedicated_workers_ttl',
        'default_job_callback_url': 'default_job_callback_url',
        'email': 'email',
        'first_name': 'first_name',
        'id': 'id',
        'job_counts': 'job_counts',
        'last_name': 'last_name'
    }

    def __init__(self, api_key=None, application_name=None, application_type=None, creation_time=None, dedicated_workers=None, dedicated_workers_max_models=None, dedicated_workers_ttl=None, default_job_callback_url=None, email=None, first_name=None, id=None, job_counts=None, last_name=None):  # noqa: E501
        """Application - a model defined in Swagger"""  # noqa: E501
        self._api_key = None
        self._application_name = None
        self._application_type = None
        self._creation_time = None
        self._dedicated_workers = None
        self._dedicated_workers_max_models = None
        self._dedicated_workers_ttl = None
        self._default_job_callback_url = None
        self._email = None
        self._first_name = None
        self._id = None
        self._job_counts = None
        self._last_name = None
        self.discriminator = None
        if api_key is not None:
            self.api_key = api_key
        if application_name is not None:
            self.application_name = application_name
        self.application_type = application_type
        if creation_time is not None:
            self.creation_time = creation_time
        if dedicated_workers is not None:
            self.dedicated_workers = dedicated_workers
        if dedicated_workers_max_models is not None:
            self.dedicated_workers_max_models = dedicated_workers_max_models
        if dedicated_workers_ttl is not None:
            self.dedicated_workers_ttl = dedicated_workers_ttl
        if default_job_callback_url is not None:
            self.default_job_callback_url = default_job_callback_url
        self.email = email
        self.first_name = first_name
        if id is not None:
            self.id = id
        if job_counts is not None:
            self.job_counts = job_counts
        self.last_name = last_name

    @property
    def api_key(self):
        """Gets the api_key of this Application.  # noqa: E501


        :return: The api_key of this Application.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Application.


        :param api_key: The api_key of this Application.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def application_name(self):
        """Gets the application_name of this Application.  # noqa: E501


        :return: The application_name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this Application.


        :param application_name: The application_name of this Application.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def application_type(self):
        """Gets the application_type of this Application.  # noqa: E501


        :return: The application_type of this Application.  # noqa: E501
        :rtype: ApplicationTypes
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this Application.


        :param application_type: The application_type of this Application.  # noqa: E501
        :type: ApplicationTypes
        """
        if application_type is None:
            raise ValueError("Invalid value for `application_type`, must not be `None`")  # noqa: E501

        self._application_type = application_type

    @property
    def creation_time(self):
        """Gets the creation_time of this Application.  # noqa: E501


        :return: The creation_time of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Application.


        :param creation_time: The creation_time of this Application.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def dedicated_workers(self):
        """Gets the dedicated_workers of this Application.  # noqa: E501


        :return: The dedicated_workers of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._dedicated_workers

    @dedicated_workers.setter
    def dedicated_workers(self, dedicated_workers):
        """Sets the dedicated_workers of this Application.


        :param dedicated_workers: The dedicated_workers of this Application.  # noqa: E501
        :type: bool
        """

        self._dedicated_workers = dedicated_workers

    @property
    def dedicated_workers_max_models(self):
        """Gets the dedicated_workers_max_models of this Application.  # noqa: E501


        :return: The dedicated_workers_max_models of this Application.  # noqa: E501
        :rtype: int
        """
        return self._dedicated_workers_max_models

    @dedicated_workers_max_models.setter
    def dedicated_workers_max_models(self, dedicated_workers_max_models):
        """Sets the dedicated_workers_max_models of this Application.


        :param dedicated_workers_max_models: The dedicated_workers_max_models of this Application.  # noqa: E501
        :type: int
        """

        self._dedicated_workers_max_models = dedicated_workers_max_models

    @property
    def dedicated_workers_ttl(self):
        """Gets the dedicated_workers_ttl of this Application.  # noqa: E501


        :return: The dedicated_workers_ttl of this Application.  # noqa: E501
        :rtype: int
        """
        return self._dedicated_workers_ttl

    @dedicated_workers_ttl.setter
    def dedicated_workers_ttl(self, dedicated_workers_ttl):
        """Sets the dedicated_workers_ttl of this Application.


        :param dedicated_workers_ttl: The dedicated_workers_ttl of this Application.  # noqa: E501
        :type: int
        """

        self._dedicated_workers_ttl = dedicated_workers_ttl

    @property
    def default_job_callback_url(self):
        """Gets the default_job_callback_url of this Application.  # noqa: E501


        :return: The default_job_callback_url of this Application.  # noqa: E501
        :rtype: str
        """
        return self._default_job_callback_url

    @default_job_callback_url.setter
    def default_job_callback_url(self, default_job_callback_url):
        """Sets the default_job_callback_url of this Application.


        :param default_job_callback_url: The default_job_callback_url of this Application.  # noqa: E501
        :type: str
        """

        self._default_job_callback_url = default_job_callback_url

    @property
    def email(self):
        """Gets the email of this Application.  # noqa: E501


        :return: The email of this Application.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Application.


        :param email: The email of this Application.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this Application.  # noqa: E501


        :return: The first_name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Application.


        :param first_name: The first_name of this Application.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501


        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.


        :param id: The id of this Application.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def job_counts(self):
        """Gets the job_counts of this Application.  # noqa: E501


        :return: The job_counts of this Application.  # noqa: E501
        :rtype: object
        """
        return self._job_counts

    @job_counts.setter
    def job_counts(self, job_counts):
        """Sets the job_counts of this Application.


        :param job_counts: The job_counts of this Application.  # noqa: E501
        :type: object
        """

        self._job_counts = job_counts

    @property
    def last_name(self):
        """Gets the last_name of this Application.  # noqa: E501


        :return: The last_name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Application.


        :param last_name: The last_name of this Application.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

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
        if issubclass(Application, dict):
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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
