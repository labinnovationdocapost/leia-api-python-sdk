# leiaapi/generated.WorkerApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_worker**](WorkerApi.md#get_worker) | **GET** /worker/{job_type} | Retrieves worker information from Leia API
[**get_workers**](WorkerApi.md#get_workers) | **GET** /worker | Retrieves worker information from Leia API

# **get_worker**
> Worker get_worker(token, job_type)

Retrieves worker information from Leia API

Retrieves worker information from Leia API 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.WorkerApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
job_type = 'job_type_example' # str | The job_type for which to get worker info

try:
    # Retrieves worker information from Leia API
    api_response = api_instance.get_worker(token, job_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerApi->get_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **job_type** | **str**| The job_type for which to get worker info | 

### Return type

[**Worker**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workers**
> list[Worker] get_workers(token)

Retrieves worker information from Leia API

Retrieves worker information from Leia API 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.WorkerApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}

try:
    # Retrieves worker information from Leia API
    api_response = api_instance.get_workers(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerApi->get_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 

### Return type

[**list[Worker]**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

