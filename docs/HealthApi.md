# leiaapi.generated.HealthApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /health | Checks Leia API health

# **health_check**
> health_check()

Checks Leia API health

Health check for the application returns a 200 HTTP status when everything is OK

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.HealthApi()

try:
    # Checks Leia API health
    api_instance.health_check()
except ApiException as e:
    print("Exception when calling HealthApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

