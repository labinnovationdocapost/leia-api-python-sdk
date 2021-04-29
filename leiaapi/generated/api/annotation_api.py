# coding: utf-8

"""
    LEIA RESTful API for AI

    Leia API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from leiaapi.generated.api_client import ApiClient


class AnnotationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_annotation(self, body, token, annotation_type, document_id, **kwargs):  # noqa: E501
        """Creates an annotation  # noqa: E501

        Creates an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation(body, token, annotation_type, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Object body: The prediction that should be associated to document in this annotation, in free form json (required)
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param AnnotationTypes annotation_type: The type of the annotation (required)
        :param str document_id: The id of the document to annotate (required)
        :param str name: The name of the annotation (for information purposes only)
        :param list[str] tags: The tags of the annotation
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_annotation_with_http_info(body, token, annotation_type, document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_annotation_with_http_info(body, token, annotation_type, document_id, **kwargs)  # noqa: E501
            return data

    def create_annotation_with_http_info(self, body, token, annotation_type, document_id, **kwargs):  # noqa: E501
        """Creates an annotation  # noqa: E501

        Creates an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_with_http_info(body, token, annotation_type, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Object body: The prediction that should be associated to document in this annotation, in free form json (required)
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param AnnotationTypes annotation_type: The type of the annotation (required)
        :param str document_id: The id of the document to annotate (required)
        :param str name: The name of the annotation (for information purposes only)
        :param list[str] tags: The tags of the annotation
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'token', 'annotation_type', 'document_id', 'name', 'tags']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_annotation`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `create_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_type' is set
        if ('annotation_type' not in params or
                params['annotation_type'] is None):
            raise ValueError("Missing the required parameter `annotation_type` when calling `create_annotation`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `create_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_id' in params:
            path_params['document_id'] = params['document_id']  # noqa: E501

        query_params = []
        if 'annotation_type' in params:
            query_params.append(('annotation_type', params['annotation_type']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
            collection_formats['tags'] = 'multi'  # noqa: E501

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{document_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_annotation(self, token, annotation_id, **kwargs):  # noqa: E501
        """Deletes an annotation  # noqa: E501

        Deletes an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation(token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (for information purposes only) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_annotation_with_http_info(token, annotation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_annotation_with_http_info(token, annotation_id, **kwargs)  # noqa: E501
            return data

    def delete_annotation_with_http_info(self, token, annotation_id, **kwargs):  # noqa: E501
        """Deletes an annotation  # noqa: E501

        Deletes an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation_with_http_info(token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (for information purposes only) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'annotation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `delete_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params or
                params['annotation_id'] is None):
            raise ValueError("Missing the required parameter `annotation_id` when calling `delete_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'annotation_id' in params:
            path_params['annotation_id'] = params['annotation_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{annotation_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_annotation(self, token, annotation_id, **kwargs):  # noqa: E501
        """Retrieves an annotation  # noqa: E501

        Retrieves an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation(token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (for information purposes only) (required)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_annotation_with_http_info(token, annotation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_annotation_with_http_info(token, annotation_id, **kwargs)  # noqa: E501
            return data

    def get_annotation_with_http_info(self, token, annotation_id, **kwargs):  # noqa: E501
        """Retrieves an annotation  # noqa: E501

        Retrieves an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation_with_http_info(token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (for information purposes only) (required)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'annotation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params or
                params['annotation_id'] is None):
            raise ValueError("Missing the required parameter `annotation_id` when calling `get_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'annotation_id' in params:
            path_params['annotation_id'] = params['annotation_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{annotation_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_annotations(self, token, **kwargs):  # noqa: E501
        """Retrieves annotations (paginated)  # noqa: E501

        Retrieves annotations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotations(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: If specified, filters the annotations id
        :param AnnotationTypes annotation_type: If specified, filters the annotations by type
        :param str name: If specified, filters the annotations by name
        :param list[str] tags: If specified, filters the annotations by tag
        :param str document_id: If specified, filters the annotations attached to a given document
        :param datetime created_after: If specified, keeps only annotations created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param datetime created_before: If specified, keeps only annotations created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param int offset: Number of the first annotation to send (pagination)
        :param int limit: Maximum number of annotation to send (pagination)
        :return: list[Annotation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_annotations_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_annotations_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def get_annotations_with_http_info(self, token, **kwargs):  # noqa: E501
        """Retrieves annotations (paginated)  # noqa: E501

        Retrieves annotations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotations_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: If specified, filters the annotations id
        :param AnnotationTypes annotation_type: If specified, filters the annotations by type
        :param str name: If specified, filters the annotations by name
        :param list[str] tags: If specified, filters the annotations by tag
        :param str document_id: If specified, filters the annotations attached to a given document
        :param datetime created_after: If specified, keeps only annotations created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param datetime created_before: If specified, keeps only annotations created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param int offset: Number of the first annotation to send (pagination)
        :param int limit: Maximum number of annotation to send (pagination)
        :return: list[Annotation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'annotation_id', 'annotation_type', 'name', 'tags', 'document_id', 'created_after', 'created_before', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_annotations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'annotation_id' in params:
            query_params.append(('annotation_id', params['annotation_id']))  # noqa: E501
        if 'annotation_type' in params:
            query_params.append(('annotation_type', params['annotation_type']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
            collection_formats['tags'] = 'multi'  # noqa: E501
        if 'document_id' in params:
            query_params.append(('document_id', params['document_id']))  # noqa: E501
        if 'created_after' in params:
            query_params.append(('created_after', params['created_after']))  # noqa: E501
        if 'created_before' in params:
            query_params.append(('created_before', params['created_before']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Annotation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tag_annotation(self, token, annotation_id, tag, **kwargs):  # noqa: E501
        """Tags an annotation  # noqa: E501

        Tags an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_annotation(token, annotation_id, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (required)
        :param str tag: The tag to add to the annotation (required)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tag_annotation_with_http_info(token, annotation_id, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.tag_annotation_with_http_info(token, annotation_id, tag, **kwargs)  # noqa: E501
            return data

    def tag_annotation_with_http_info(self, token, annotation_id, tag, **kwargs):  # noqa: E501
        """Tags an annotation  # noqa: E501

        Tags an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_annotation_with_http_info(token, annotation_id, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (required)
        :param str tag: The tag to add to the annotation (required)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'annotation_id', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `tag_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params or
                params['annotation_id'] is None):
            raise ValueError("Missing the required parameter `annotation_id` when calling `tag_annotation`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `tag_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'annotation_id' in params:
            path_params['annotation_id'] = params['annotation_id']  # noqa: E501
        if 'tag' in params:
            path_params['tag'] = params['tag']  # noqa: E501

        query_params = []

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{annotation_id}/tag/{tag}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def untag_annotation(self, token, annotation_id, tag, **kwargs):  # noqa: E501
        """Untags an annotation  # noqa: E501

        Untags an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.untag_annotation(token, annotation_id, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (required)
        :param str tag: The tag to delete from the annotation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.untag_annotation_with_http_info(token, annotation_id, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.untag_annotation_with_http_info(token, annotation_id, tag, **kwargs)  # noqa: E501
            return data

    def untag_annotation_with_http_info(self, token, annotation_id, tag, **kwargs):  # noqa: E501
        """Untags an annotation  # noqa: E501

        Untags an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.untag_annotation_with_http_info(token, annotation_id, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation (required)
        :param str tag: The tag to delete from the annotation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'annotation_id', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method untag_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `untag_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params or
                params['annotation_id'] is None):
            raise ValueError("Missing the required parameter `annotation_id` when calling `untag_annotation`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `untag_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'annotation_id' in params:
            path_params['annotation_id'] = params['annotation_id']  # noqa: E501
        if 'tag' in params:
            path_params['tag'] = params['tag']  # noqa: E501

        query_params = []

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{annotation_id}/tag/{tag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_annotation(self, body, token, annotation_id, **kwargs):  # noqa: E501
        """Updates an annotation  # noqa: E501

        Updates an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation(body, token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Object body: The new prediction that should be associated to document in this annotation, in free form json (required)
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation to modify (required)
        :param str name: The new name of the annotation (won't change if not set)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_annotation_with_http_info(body, token, annotation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_annotation_with_http_info(body, token, annotation_id, **kwargs)  # noqa: E501
            return data

    def update_annotation_with_http_info(self, body, token, annotation_id, **kwargs):  # noqa: E501
        """Updates an annotation  # noqa: E501

        Updates an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation_with_http_info(body, token, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Object body: The new prediction that should be associated to document in this annotation, in free form json (required)
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str annotation_id: The id of the annotation to modify (required)
        :param str name: The new name of the annotation (won't change if not set)
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'token', 'annotation_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_annotation`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `update_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params or
                params['annotation_id'] is None):
            raise ValueError("Missing the required parameter `annotation_id` when calling `update_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'annotation_id' in params:
            path_params['annotation_id'] = params['annotation_id']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/annotation/{annotation_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
