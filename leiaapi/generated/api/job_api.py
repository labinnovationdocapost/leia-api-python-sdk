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


class JobApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_job(self, token, job_id, **kwargs):  # noqa: E501
        """Cancels a job in Leia API  # noqa: E501

        Cancels a job in Leia API (This will not really delete it, just mark it as cancelled, so dependent jobs will fail)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_job(token, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_job_with_http_info(token, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_job_with_http_info(token, job_id, **kwargs)  # noqa: E501
            return data

    def cancel_job_with_http_info(self, token, job_id, **kwargs):  # noqa: E501
        """Cancels a job in Leia API  # noqa: E501

        Cancels a job in Leia API (This will not really delete it, just mark it as cancelled, so dependent jobs will fail)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_job_with_http_info(token, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `cancel_job`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `cancel_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

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
            '/job/{job_id}', 'DELETE',
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

    def create_conditional_job(self, token, execute_after_id, **kwargs):  # noqa: E501
        """Asynchronously and conditionaly applies model(s) on documents  # noqa: E501

        Asynchronously runs one or more list of jobs on accessible documents and returns a Job.<br /> The list of jobs to run and the documents on which they should be run will be chosen depending on the rules parameter that is set in the body of the request and the result of the execute_after_id job.<br /> Rules should be a map[string,object] where the key is a user chosen id and the value is a list of objects containing the same parameters as normal calls to /model/{model_id}/apply{document_ids} or /document/{document_ids}/transform/{output_type} and a conditions field.<br /> If all the field/values in the conditions of a rule are contained as is in the result of the execute_after_id job, then the list of jobs will be executed in order with the given parameters, each job depending on the previous one in the list, else it won't be executed at all<br /> Syntax for conditions is as follows:   * \"field_name\" : value In which case the field field_name must be equal to the value for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": {\"operator\" : value} Where operator is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": [{\"operator_1\" : value_1}...{\"operator_n\" : value_n}] Where operator_i is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for all items in the list for the job to be executed. value_i can be any valid json type (int, float, string...). {\"$eq\" : value_i} can be abbreviated as value_i in the list.  You can keep the document_ids field of any job empty apart for the first job of a rule. If it is, the job will use the results of previous job's as an input if no tag is set, or the document_ids of the execute_after_id job + tag if tag is set.<br /> If the conditions are not mutually exclusive, 2 or more models may be executed.<br /> The result will be sent back as a map of results where the key is the rule id, and containing one entry for list of jobs that was executed. This entry will contain all the results of the executed jobs, in execution order<br /> This is mostly but not necessarily meant to be used after a classifier model, so that an execution path can be chosen automatically depending on the result of the classification.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_conditional_job(token, execute_after_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str execute_after_id: The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail (required)
        :param ConditionalBody body: Contains the rules to choose the model to apply. All the previous query parameters can also be passed as JSON in the body of the request
        :param str callback_url: Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback.
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_conditional_job_with_http_info(token, execute_after_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_conditional_job_with_http_info(token, execute_after_id, **kwargs)  # noqa: E501
            return data

    def create_conditional_job_with_http_info(self, token, execute_after_id, **kwargs):  # noqa: E501
        """Asynchronously and conditionaly applies model(s) on documents  # noqa: E501

        Asynchronously runs one or more list of jobs on accessible documents and returns a Job.<br /> The list of jobs to run and the documents on which they should be run will be chosen depending on the rules parameter that is set in the body of the request and the result of the execute_after_id job.<br /> Rules should be a map[string,object] where the key is a user chosen id and the value is a list of objects containing the same parameters as normal calls to /model/{model_id}/apply{document_ids} or /document/{document_ids}/transform/{output_type} and a conditions field.<br /> If all the field/values in the conditions of a rule are contained as is in the result of the execute_after_id job, then the list of jobs will be executed in order with the given parameters, each job depending on the previous one in the list, else it won't be executed at all<br /> Syntax for conditions is as follows:   * \"field_name\" : value In which case the field field_name must be equal to the value for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": {\"operator\" : value} Where operator is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": [{\"operator_1\" : value_1}...{\"operator_n\" : value_n}] Where operator_i is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for all items in the list for the job to be executed. value_i can be any valid json type (int, float, string...). {\"$eq\" : value_i} can be abbreviated as value_i in the list.  You can keep the document_ids field of any job empty apart for the first job of a rule. If it is, the job will use the results of previous job's as an input if no tag is set, or the document_ids of the execute_after_id job + tag if tag is set.<br /> If the conditions are not mutually exclusive, 2 or more models may be executed.<br /> The result will be sent back as a map of results where the key is the rule id, and containing one entry for list of jobs that was executed. This entry will contain all the results of the executed jobs, in execution order<br /> This is mostly but not necessarily meant to be used after a classifier model, so that an execution path can be chosen automatically depending on the result of the classification.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_conditional_job_with_http_info(token, execute_after_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str execute_after_id: The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail (required)
        :param ConditionalBody body: Contains the rules to choose the model to apply. All the previous query parameters can also be passed as JSON in the body of the request
        :param str callback_url: Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback.
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'execute_after_id', 'body', 'callback_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_conditional_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `create_conditional_job`")  # noqa: E501
        # verify the required parameter 'execute_after_id' is set
        if ('execute_after_id' not in params or
                params['execute_after_id'] is None):
            raise ValueError("Missing the required parameter `execute_after_id` when calling `create_conditional_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execute_after_id' in params:
            path_params['execute_after_id'] = params['execute_after_id']  # noqa: E501

        query_params = []
        if 'callback_url' in params:
            query_params.append(('callback_url', params['callback_url']))  # noqa: E501

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
            '/job/conditional/{execute_after_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job(self, token, job_id, **kwargs):  # noqa: E501
        """Retrieves a job from Leia API  # noqa: E501

        Retrieves a job from Leia API   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job(token, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job to retrieve (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_with_http_info(token, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_with_http_info(token, job_id, **kwargs)  # noqa: E501
            return data

    def get_job_with_http_info(self, token, job_id, **kwargs):  # noqa: E501
        """Retrieves a job from Leia API  # noqa: E501

        Retrieves a job from Leia API   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_with_http_info(token, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job to retrieve (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_job`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

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
            '/job/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job_statuses(self, token, job_ids, **kwargs):  # noqa: E501
        """Retrieves job statuses from Leia API  # noqa: E501

        Retrieves a list of job statuses from Leia API   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_statuses(token, job_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param list[str] job_ids: The ids of the jobs to retrieve, comma separated (required)
        :return: dict(str, Statuses)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_statuses_with_http_info(token, job_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_statuses_with_http_info(token, job_ids, **kwargs)  # noqa: E501
            return data

    def get_job_statuses_with_http_info(self, token, job_ids, **kwargs):  # noqa: E501
        """Retrieves job statuses from Leia API  # noqa: E501

        Retrieves a list of job statuses from Leia API   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_statuses_with_http_info(token, job_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param list[str] job_ids: The ids of the jobs to retrieve, comma separated (required)
        :return: dict(str, Statuses)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'job_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job_statuses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_job_statuses`")  # noqa: E501
        # verify the required parameter 'job_ids' is set
        if ('job_ids' not in params or
                params['job_ids'] is None):
            raise ValueError("Missing the required parameter `job_ids` when calling `get_job_statuses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_ids' in params:
            path_params['job_ids'] = params['job_ids']  # noqa: E501
            collection_formats['job_ids'] = ''  # noqa: E501

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
            '/job/{job_ids}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, Statuses)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_jobs(self, token, **kwargs):  # noqa: E501
        """Retrieves jobs (paginated)  # noqa: E501

        Get jobs from the system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jobs(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job
        :param str application_id: The id of the owner of the documents processed by this job
        :param JobTypes job_type: The type of the job (predict, pdf-images, image-text or transform)
        :param str model_id: The model used by the job (only for predict jobs)
        :param str document_id: The document that this the job is processing
        :param str execute_after_id: The job that is a prerequisite for this job to run
        :param str parent_job_id: The job that is the parent of this job
        :param Statuses status: The status of the job
        :param datetime created_after: If specified, keeps only jobs created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param datetime created_before: If specified, keeps only jobs created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param str sort: If specified, sorts the jobs by a list of existing parameters separated by commas. Can be 'submitter_id', 'application_id', 'creation_time', 'starting_time', 'finished_time', 'job_type', 'model_id', 'document_ids', 'status', 'parent_job_id'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order.
        :param int offset: Number of the first job to send (pagination)
        :param int limit: Maximum number of jobs to send (pagination)
        :return: list[Job]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_jobs_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_jobs_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def get_jobs_with_http_info(self, token, **kwargs):  # noqa: E501
        """Retrieves jobs (paginated)  # noqa: E501

        Get jobs from the system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jobs_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: The login token obtained via GET /login/{api_key} (required)
        :param str job_id: The id of the job
        :param str application_id: The id of the owner of the documents processed by this job
        :param JobTypes job_type: The type of the job (predict, pdf-images, image-text or transform)
        :param str model_id: The model used by the job (only for predict jobs)
        :param str document_id: The document that this the job is processing
        :param str execute_after_id: The job that is a prerequisite for this job to run
        :param str parent_job_id: The job that is the parent of this job
        :param Statuses status: The status of the job
        :param datetime created_after: If specified, keeps only jobs created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param datetime created_before: If specified, keeps only jobs created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss)
        :param str sort: If specified, sorts the jobs by a list of existing parameters separated by commas. Can be 'submitter_id', 'application_id', 'creation_time', 'starting_time', 'finished_time', 'job_type', 'model_id', 'document_ids', 'status', 'parent_job_id'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order.
        :param int offset: Number of the first job to send (pagination)
        :param int limit: Maximum number of jobs to send (pagination)
        :return: list[Job]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'job_id', 'application_id', 'job_type', 'model_id', 'document_id', 'execute_after_id', 'parent_job_id', 'status', 'created_after', 'created_before', 'sort', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_jobs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_jobs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('job_id', params['job_id']))  # noqa: E501
        if 'application_id' in params:
            query_params.append(('application_id', params['application_id']))  # noqa: E501
        if 'job_type' in params:
            query_params.append(('job_type', params['job_type']))  # noqa: E501
        if 'model_id' in params:
            query_params.append(('model_id', params['model_id']))  # noqa: E501
        if 'document_id' in params:
            query_params.append(('document_id', params['document_id']))  # noqa: E501
        if 'execute_after_id' in params:
            query_params.append(('execute_after_id', params['execute_after_id']))  # noqa: E501
        if 'parent_job_id' in params:
            query_params.append(('parent_job_id', params['parent_job_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'created_after' in params:
            query_params.append(('created_after', params['created_after']))  # noqa: E501
        if 'created_before' in params:
            query_params.append(('created_before', params['created_before']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
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
            '/job', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Job]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
