# leiaapi.generated.WorkerAdminApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kill_worker**](WorkerAdminApi.md#kill_worker) | **DELETE** /worker/{job_type} | Kills a worker (admin only)

# **kill_worker**
> kill_worker(token, job_type)

Kills a worker (admin only)

Kills a worker for a given job_type. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.WorkerAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
job_type = 'job_type_example' # str | The job_type for which to kill a worker

try:
    # Kills a worker (admin only)
    api_instance.kill_worker(token, job_type)
except ApiException as e:
    print("Exception when calling WorkerAdminApi->kill_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **job_type** | **str**| The job_type for which to kill a worker | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

