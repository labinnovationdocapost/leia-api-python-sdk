# leiaapi/generated.ApplicationApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_application**](ApplicationApi.md#login_application) | **GET** /login/{api_key} | Logs into Leia API
[**logout_application**](ApplicationApi.md#logout_application) | **GET** /logout | Logs out from Leia API
[**who_am_i**](ApplicationApi.md#who_am_i) | **GET** /whoami | Gets the currently connected application

# **login_application**
> LoginToken login_application(api_key)

Logs into Leia API

Logs an application into Leia API using its API key. Returns a token that will have to be set in all subsequent requests, to identify the logged in application 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.ApplicationApi()
api_key = 'api_key_example' # str | The API key

try:
    # Logs into Leia API
    api_response = api_instance.login_application(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->login_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | [**str**](.md)| The API key | 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_application**
> logout_application(token)

Logs out from Leia API

Logs a connected application out of Leia API using its token 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.ApplicationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}

try:
    # Logs out from Leia API
    api_instance.logout_application(token)
except ApiException as e:
    print("Exception when calling ApplicationApi->logout_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> Application who_am_i(token)

Gets the currently connected application

Gets the currently connected application. Also use this method to reset token timeout 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.ApplicationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}

try:
    # Gets the currently connected application
    api_response = api_instance.who_am_i(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->who_am_i: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

