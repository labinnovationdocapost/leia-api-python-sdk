# leiaapi/generated.JobAdminApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_cancel_job**](JobAdminApi.md#admin_cancel_job) | **DELETE** /admin/{submitter_id}/job/{job_id} | Cancels a job in Leia API (admin only)
[**admin_create_conditional_job**](JobAdminApi.md#admin_create_conditional_job) | **POST** /admin/{application_id}/job/conditional/{execute_after_id} | Asynchronously and conditionaly applies model(s) on documents (admin only)
[**admin_get_job**](JobAdminApi.md#admin_get_job) | **GET** /admin/{submitter_id}/job/{job_id} | Retrieves a job from Leia API (admin only)
[**admin_get_job_statuses**](JobAdminApi.md#admin_get_job_statuses) | **GET** /admin/{submitter_id}/job/{job_ids}/status | Retrieves job statuses from Leia API (admin only)
[**admin_get_jobs**](JobAdminApi.md#admin_get_jobs) | **GET** /admin/job | Retrieves jobs (admin only) (paginated)

# **admin_cancel_job**
> admin_cancel_job(token, submitter_id, job_id)

Cancels a job in Leia API (admin only)

Cancels a job in Leia API (This will not really delete it, just mark it as cancelled, so dependent jobs will fail). This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.JobAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
submitter_id = 'submitter_id_example' # str | The application which submitted the job
job_id = 'job_id_example' # str | The id of the job to delete

try:
    # Cancels a job in Leia API (admin only)
    api_instance.admin_cancel_job(token, submitter_id, job_id)
except ApiException as e:
    print("Exception when calling JobAdminApi->admin_cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **submitter_id** | **str**| The application which submitted the job | 
 **job_id** | **str**| The id of the job to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_conditional_job**
> Job admin_create_conditional_job(token, application_id, execute_after_id, body=body, callback_url=callback_url)

Asynchronously and conditionaly applies model(s) on documents (admin only)

This method is only accessible to admins.<br /> Asynchronously runs one or more list of jobs on accessible documents and returns a Job.<br /> The list of jobs to run and the documents on which they should be run will be chosen depending on the rules parameter that is set in the body of the request and the result of the execute_after_id job.<br /> Rules should be a map[string,object] where the key is a user chosen id and the value is a list of objects containing the same parameters as normal calls to /admin/{application_id}/model/{model_id}/apply{document_ids} or /admin/{application_id}/document/{document_ids}/transform/{output_type} and a conditions field.<br /> If all the field/values in the conditions of a rule are contained as is in the result of the execute_after_id job, then the list of jobs will be executed in order with the given parameters, each job depending on the previous one in the list, else it won't be executed at all<br /> Syntax for conditions is as follows:   * \"field_name\" : value In which case the field field_name must be equal to the value for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": {\"operator\" : value} Where operator is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for the job to be executed. value can be any valid json type (int, float, string...)   * \"field_name\": [{\"operator_1\" : value_1}...{\"operator_n\" : value_n}] Where operator_i is a [Mongo like comparison operator](https://docs.mongodb.com/manual/reference/operator/query-comparison/). In this case the comparison between field field_name's value must be true for all items in the list for the job to be executed. value_i can be any valid json type (int, float, string...). {\"$eq\" : value_i} can be abbreviated as value_i in the list.  You can keep the document_ids field of any job empty. If it is, the job will use the results of previous job's as an input if no tag is set, or the document_ids of the execute_after_id job + tag if tag is set.<br /> If the conditions are not mutually exclusive, 2 or more models may be executed.<br /> The result will be sent back as a map of results where the key is the rule id, and containing one entry for list of jobs that was executed. This entry will contain all the results of the executed jobs, in execution order<br /> This is mostly but not necessarily meant to be used after a classifier model, so that an execution path can be chosen automatically depending on the result of the classification. 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.JobAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the models belongs
execute_after_id = 'execute_after_id_example' # str | The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail
body = leiaapi/generated.ConditionalBody() # ConditionalBody | Contains the rules to choose the model to apply. All the previous query parameters can also be passed as JSON in the body of the request (optional)
callback_url = 'callback_url_example' # str | Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. (optional)

try:
    # Asynchronously and conditionaly applies model(s) on documents (admin only)
    api_response = api_instance.admin_create_conditional_job(token, application_id, execute_after_id, body=body, callback_url=callback_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobAdminApi->admin_create_conditional_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the models belongs | 
 **execute_after_id** | **str**| The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail | 
 **body** | [**ConditionalBody**](ConditionalBody.md)| Contains the rules to choose the model to apply. All the previous query parameters can also be passed as JSON in the body of the request | [optional] 
 **callback_url** | **str**| Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_job**
> Job admin_get_job(token, submitter_id, job_id)

Retrieves a job from Leia API (admin only)

Retrieves a job from Leia API. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.JobAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
submitter_id = 'submitter_id_example' # str | The application which submitted the job
job_id = 'job_id_example' # str | The id of the job to retrieve

try:
    # Retrieves a job from Leia API (admin only)
    api_response = api_instance.admin_get_job(token, submitter_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobAdminApi->admin_get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **submitter_id** | **str**| The application which submitted the job | 
 **job_id** | **str**| The id of the job to retrieve | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_job_statuses**
> dict(str, Statuses) admin_get_job_statuses(token, submitter_id, job_ids)

Retrieves job statuses from Leia API (admin only)

Retrieves a list of job statuses from Leia API. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.JobAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
submitter_id = 'submitter_id_example' # str | The id of the submitter of the job
job_ids = ['job_ids_example'] # list[str] | The ids of the jobs to retrieve, comma separated

try:
    # Retrieves job statuses from Leia API (admin only)
    api_response = api_instance.admin_get_job_statuses(token, submitter_id, job_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobAdminApi->admin_get_job_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **submitter_id** | **str**| The id of the submitter of the job | 
 **job_ids** | [**list[str]**](str.md)| The ids of the jobs to retrieve, comma separated | 

### Return type

[**dict(str, Statuses)**](Statuses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_jobs**
> list[Job] admin_get_jobs(token, job_id=job_id, submitter_id=submitter_id, application_id=application_id, job_type=job_type, model_id=model_id, document_id=document_id, execute_after_id=execute_after_id, parent_job_id=parent_job_id, status=status, created_after=created_after, created_before=created_before, sort=sort, offset=offset, limit=limit)

Retrieves jobs (admin only) (paginated)

Get jobs from the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.JobAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
job_id = 'job_id_example' # str | The id of the job (optional)
submitter_id = 'submitter_id_example' # str | The id of the submitter of the job (optional)
application_id = 'application_id_example' # str | The id of the owner of the documents processed by this job (optional)
job_type = leiaapi/generated.JobTypes() # JobTypes | The type of the job (predict, pdf-images, image-text or transform) (optional)
model_id = 'model_id_example' # str | The model used by the job (only for predict jobs) (optional)
document_id = 'document_id_example' # str | The document that this the job is processing (optional)
execute_after_id = 'execute_after_id_example' # str | The job that is a prerequisite for this job to run (optional)
parent_job_id = 'parent_job_id_example' # str | The job that is the parent of this job (optional)
status = leiaapi/generated.Statuses() # Statuses | The status of the job (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only jobs created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only jobs created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
sort = 'sort_example' # str | If specified, sorts the jobs by a list of existing parameters separated by commas. Can be 'submitter_id', 'application_id', 'creation_time', 'starting_time', 'finished_time', 'job_type', 'model_id', 'document_ids', 'status', 'parent_job_id'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order. (optional)
offset = 56 # int | Number of the first job to send (pagination) (optional)
limit = 56 # int | Maximum number of jobs to send (pagination) (optional)

try:
    # Retrieves jobs (admin only) (paginated)
    api_response = api_instance.admin_get_jobs(token, job_id=job_id, submitter_id=submitter_id, application_id=application_id, job_type=job_type, model_id=model_id, document_id=document_id, execute_after_id=execute_after_id, parent_job_id=parent_job_id, status=status, created_after=created_after, created_before=created_before, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobAdminApi->admin_get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **job_id** | **str**| The id of the job | [optional] 
 **submitter_id** | **str**| The id of the submitter of the job | [optional] 
 **application_id** | **str**| The id of the owner of the documents processed by this job | [optional] 
 **job_type** | [**JobTypes**](.md)| The type of the job (predict, pdf-images, image-text or transform) | [optional] 
 **model_id** | **str**| The model used by the job (only for predict jobs) | [optional] 
 **document_id** | **str**| The document that this the job is processing | [optional] 
 **execute_after_id** | **str**| The job that is a prerequisite for this job to run | [optional] 
 **parent_job_id** | **str**| The job that is the parent of this job | [optional] 
 **status** | [**Statuses**](.md)| The status of the job | [optional] 
 **created_after** | **datetime**| If specified, keeps only jobs created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only jobs created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **sort** | **str**| If specified, sorts the jobs by a list of existing parameters separated by commas. Can be &#x27;submitter_id&#x27;, &#x27;application_id&#x27;, &#x27;creation_time&#x27;, &#x27;starting_time&#x27;, &#x27;finished_time&#x27;, &#x27;job_type&#x27;, &#x27;model_id&#x27;, &#x27;document_ids&#x27;, &#x27;status&#x27;, &#x27;parent_job_id&#x27;. Sorts in ascending order by default. If a parameter is preceded by &#x27;-&#x27;, it is sorted in descending order. | [optional] 
 **offset** | **int**| Number of the first job to send (pagination) | [optional] 
 **limit** | **int**| Maximum number of jobs to send (pagination) | [optional] 

### Return type

[**list[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

