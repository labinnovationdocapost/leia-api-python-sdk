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
from leiaapi.generated.api.annotation_api import AnnotationApi  # noqa: E501
from leiaapi.generated.rest import ApiException


class TestAnnotationApi(unittest.TestCase):
    """AnnotationApi unit test stubs"""

    def setUp(self):
        self.api = AnnotationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_annotation(self):
        """Test case for create_annotation

        Creates an annotation  # noqa: E501
        """
        pass

    def test_delete_annotation(self):
        """Test case for delete_annotation

        Deletes an annotation  # noqa: E501
        """
        pass

    def test_get_annotation(self):
        """Test case for get_annotation

        Retrieves an annotation  # noqa: E501
        """
        pass

    def test_get_annotations(self):
        """Test case for get_annotations

        Retrieves annotations (paginated)  # noqa: E501
        """
        pass

    def test_tag_annotation(self):
        """Test case for tag_annotation

        Tags an annotation  # noqa: E501
        """
        pass

    def test_untag_annotation(self):
        """Test case for untag_annotation

        Untags an annotation  # noqa: E501
        """
        pass

    def test_update_annotation(self):
        """Test case for update_annotation

        Updates an annotation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
