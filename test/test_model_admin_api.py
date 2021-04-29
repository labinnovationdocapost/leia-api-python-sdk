# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import leiaapi.generated
from leiaapi.generated.api.model_admin_api import ModelAdminApi  # noqa: E501
from leiaapi.generated.rest import ApiException


class TestModelAdminApi(unittest.TestCase):
    """ModelAdminApi unit test stubs"""

    def setUp(self):
        self.api = ModelAdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_apply_model_async(self):
        """Test case for admin_apply_model_async

        Asynchronously applies a model on documents (admin only)  # noqa: E501
        """
        pass

    def test_admin_create_model(self):
        """Test case for admin_create_model

        Adds a new model to the system (admin only)  # noqa: E501
        """
        pass

    def test_admin_delete_model(self):
        """Test case for admin_delete_model

        Deletes a model (admin only)  # noqa: E501
        """
        pass

    def test_admin_edit_model(self):
        """Test case for admin_edit_model

        Modifies an existing model in the system (admin only)  # noqa: E501
        """
        pass

    def test_admin_get_model(self):
        """Test case for admin_get_model

        Get a model (admin only)  # noqa: E501
        """
        pass

    def test_admin_get_model_contents(self):
        """Test case for admin_get_model_contents

        Get a model (admin only)  # noqa: E501
        """
        pass

    def test_admin_get_models(self):
        """Test case for admin_get_models

        Lists models (admin only) (paginated))  # noqa: E501
        """
        pass

    def test_admin_tag_model(self):
        """Test case for admin_tag_model

        Tags a model (admin only)  # noqa: E501
        """
        pass

    def test_admin_train_model_async(self):
        """Test case for admin_train_model_async

        Asynchronously trains a model on documents (admin only)  # noqa: E501
        """
        pass

    def test_admin_untag_model(self):
        """Test case for admin_untag_model

        Untags a model (admin only)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
