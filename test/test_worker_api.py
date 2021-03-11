# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sebastien.favre@docapost.fr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import leiaapi.generated
from leiaapi.generated.api.worker_api import WorkerApi  # noqa: E501
from leiaapi.generated.rest import ApiException


class TestWorkerApi(unittest.TestCase):
    """WorkerApi unit test stubs"""

    def setUp(self):
        self.api = WorkerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_worker(self):
        """Test case for get_worker

        Retrieves worker information from Leia API  # noqa: E501
        """
        pass

    def test_get_workers(self):
        """Test case for get_workers

        Retrieves worker information from Leia API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
