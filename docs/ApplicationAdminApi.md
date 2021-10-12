# leiaapi.generated.ApplicationAdminApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_create_application**](ApplicationAdminApi.md#admin_create_application) | **POST** /admin/application | Adds a new application to the system (admin only)
[**admin_delete_always_on_schedule**](ApplicationAdminApi.md#admin_delete_always_on_schedule) | **DELETE** /admin/application/{application_id}/always_on_schedules/{always_on_schedule_id} | Removes a schedule from an application
[**admin_delete_application**](ApplicationAdminApi.md#admin_delete_application) | **DELETE** /admin/application/{application_id} | Deletes an application (admin only)
[**admin_edit_application**](ApplicationAdminApi.md#admin_edit_application) | **PATCH** /admin/application/{application_id} | Modifies an existing application in the system (admin only)
[**admin_get_application**](ApplicationAdminApi.md#admin_get_application) | **GET** /admin/application/{application_id} | Retrieves an application (admin only)
[**admin_get_applications**](ApplicationAdminApi.md#admin_get_applications) | **GET** /admin/application | Retrieves applications (admin only) (paginated)
[**admin_reset_api_key**](ApplicationAdminApi.md#admin_reset_api_key) | **POST** /admin/application/{application_id}/reset_api_key | Resets an API key (admin only)

# **admin_create_application**
> Application admin_create_application(token, body=body)

Adds a new application to the system (admin only)

Adds a new application to the system. This method is only accessible to admins. An API key will be generated for the new application when calling this method. Note or store it carefully, it will not be recoverable after this call.

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
body = leiaapi.generated.Application() # Application |  (optional)

try:
    # Adds a new application to the system (admin only)
    api_response = api_instance.admin_create_application(token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **body** | [**Application**](Application.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_always_on_schedule**
> admin_delete_always_on_schedule(token, application_id, always_on_schedule_id)

Removes a schedule from an application

Removes a schedule from an application

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The id of the application
always_on_schedule_id = 'always_on_schedule_id_example' # str | The id of the schedule to delete

try:
    # Removes a schedule from an application
    api_instance.admin_delete_always_on_schedule(token, application_id, always_on_schedule_id)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_delete_always_on_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The id of the application | 
 **always_on_schedule_id** | **str**| The id of the schedule to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_application**
> admin_delete_application(token, application_id)

Deletes an application (admin only)

Retrieves a new application from the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The id of the application to delete

try:
    # Deletes an application (admin only)
    api_instance.admin_delete_application(token, application_id)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The id of the application to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_edit_application**
> Application admin_edit_application(token, application_id, application_name=application_name, email=email, first_name=first_name, last_name=last_name, default_job_callback_url=default_job_callback_url, dedicated_workers=dedicated_workers, dedicated_workers_ttl=dedicated_workers_ttl, dedicated_workers_max_models=dedicated_workers_max_models, reduce_callback_payloads=reduce_callback_payloads, always_on_number=always_on_number, always_on_start_days=always_on_start_days, always_on_start_hour=always_on_start_hour, always_on_stop_hour=always_on_stop_hour, always_on_start_minute=always_on_start_minute, always_on_stop_minute=always_on_stop_minute, always_on_workers_model_ids=always_on_workers_model_ids)

Modifies an existing application in the system (admin only)

Modifies an application already in the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to modify
application_name = 'application_name_example' # str | The new name of the application (optional)
email = 'email_example' # str | The new email of the application (optional)
first_name = 'first_name_example' # str | The new first name of the application (optional)
last_name = 'last_name_example' # str | The new last name of the application (optional)
default_job_callback_url = 'default_job_callback_url_example' # str | The new default_job_callback_url of the application (optional)
dedicated_workers = true # bool | Should this application use dedicated workers ? (optional)
dedicated_workers_ttl = 56 # int | When using dedicated workers, TTL of the worker (in seconds) (optional)
dedicated_workers_max_models = 56 # int | When using dedicated workers, maximum number of models loaded at the same time (optional)
reduce_callback_payloads = true # bool | Specifies if the callback should be sent as is, or if the potential base64 encoded documents generated should be saved as sub documents of the original document (optional)
always_on_number = 56 # int | Adds a schedule for always on workers. Will start number always on workers when start time happens and stop them at stop time. (Check always_on_* parameters to set other parameters) (optional)
always_on_start_days = [56] # list[int] | Adds a schedule for always on workers. Set the day(s) of the week at which the worker will start (1 is Monday, 7 is Sunday, comma separated). Stop day will be the same day. (Check always_on_* parameters to set other parameters) (optional)
always_on_start_hour = 56 # int | Adds a schedule for always on workers. Set the hour at which the worker will start (between 0 and 23). (Check always_on_* parameters to set other parameters) (optional)
always_on_stop_hour = 56 # int | Adds a schedule for always on workers. Set the hour at which the worker will stop (between 0 and 23, stop must happen after start). (Check always_on_* parameters to set other parameters) (optional)
always_on_start_minute = 56 # int | Adds a schedule for always on workers. Set the minute at which the worker will start (between 0 and 59). (Check always_on_* parameters to set other parameters) (optional)
always_on_stop_minute = 56 # int | Adds a schedule for always on workers. Set the minute at which the worker will stop (between 0 and 59, stop must happen after start). (Check always_on_* parameters to set other parameters) (optional)
always_on_workers_model_ids = ['always_on_workers_model_ids_example'] # list[str] | When using dedicated workers with always on schedule, the models that should be loaded on start of the worker (optional)

try:
    # Modifies an existing application in the system (admin only)
    api_response = api_instance.admin_edit_application(token, application_id, application_name=application_name, email=email, first_name=first_name, last_name=last_name, default_job_callback_url=default_job_callback_url, dedicated_workers=dedicated_workers, dedicated_workers_ttl=dedicated_workers_ttl, dedicated_workers_max_models=dedicated_workers_max_models, reduce_callback_payloads=reduce_callback_payloads, always_on_number=always_on_number, always_on_start_days=always_on_start_days, always_on_start_hour=always_on_start_hour, always_on_stop_hour=always_on_stop_hour, always_on_start_minute=always_on_start_minute, always_on_stop_minute=always_on_stop_minute, always_on_workers_model_ids=always_on_workers_model_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_edit_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to modify | 
 **application_name** | **str**| The new name of the application | [optional] 
 **email** | **str**| The new email of the application | [optional] 
 **first_name** | **str**| The new first name of the application | [optional] 
 **last_name** | **str**| The new last name of the application | [optional] 
 **default_job_callback_url** | **str**| The new default_job_callback_url of the application | [optional] 
 **dedicated_workers** | **bool**| Should this application use dedicated workers ? | [optional] 
 **dedicated_workers_ttl** | **int**| When using dedicated workers, TTL of the worker (in seconds) | [optional] 
 **dedicated_workers_max_models** | **int**| When using dedicated workers, maximum number of models loaded at the same time | [optional] 
 **reduce_callback_payloads** | **bool**| Specifies if the callback should be sent as is, or if the potential base64 encoded documents generated should be saved as sub documents of the original document | [optional] 
 **always_on_number** | **int**| Adds a schedule for always on workers. Will start number always on workers when start time happens and stop them at stop time. (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_start_days** | [**list[int]**](int.md)| Adds a schedule for always on workers. Set the day(s) of the week at which the worker will start (1 is Monday, 7 is Sunday, comma separated). Stop day will be the same day. (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_start_hour** | **int**| Adds a schedule for always on workers. Set the hour at which the worker will start (between 0 and 23). (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_stop_hour** | **int**| Adds a schedule for always on workers. Set the hour at which the worker will stop (between 0 and 23, stop must happen after start). (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_start_minute** | **int**| Adds a schedule for always on workers. Set the minute at which the worker will start (between 0 and 59). (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_stop_minute** | **int**| Adds a schedule for always on workers. Set the minute at which the worker will stop (between 0 and 59, stop must happen after start). (Check always_on_* parameters to set other parameters) | [optional] 
 **always_on_workers_model_ids** | [**list[str]**](str.md)| When using dedicated workers with always on schedule, the models that should be loaded on start of the worker | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_application**
> Application admin_get_application(token, application_id)

Retrieves an application (admin only)

Retrieves a new application from the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The id of the application to retrieve

try:
    # Retrieves an application (admin only)
    api_response = api_instance.admin_get_application(token, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The id of the application to retrieve | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_applications**
> list[Application] admin_get_applications(token, application_id=application_id, email=email, application_name=application_name, first_name=first_name, last_name=last_name, application_type=application_type, created_after=created_after, created_before=created_before, dedicated_workers=dedicated_workers, offset=offset, limit=limit, sort=sort)

Retrieves applications (admin only) (paginated)

Retrieves applications from the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | If specified, filters by application id (optional)
email = 'email_example' # str | If specified, filters by application email (optional)
application_name = 'application_name_example' # str | If specified, filters by application name (optional)
first_name = 'first_name_example' # str | If specified, filters by application first_name (optional)
last_name = 'last_name_example' # str | If specified, filters by application last_name (optional)
application_type = leiaapi.generated.ApplicationTypes() # ApplicationTypes | If specified, filters by application application_type (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only applications created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only applications created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
dedicated_workers = true # bool | If specified, filters by dedicated_workers value (optional)
offset = 56 # int | Number of the first document to send (pagination) (optional)
limit = 56 # int | Maximum number of documents to send (pagination) (optional)
sort = 'sort_example' # str | If specified, sorts the applications by a list of existing parameters separated by commas. Can be 'application_name', 'application_type', 'creation_time', 'first_name', 'last_name', 'email', 'dedicated_workers'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order. (optional)

try:
    # Retrieves applications (admin only) (paginated)
    api_response = api_instance.admin_get_applications(token, application_id=application_id, email=email, application_name=application_name, first_name=first_name, last_name=last_name, application_type=application_type, created_after=created_after, created_before=created_before, dedicated_workers=dedicated_workers, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| If specified, filters by application id | [optional] 
 **email** | **str**| If specified, filters by application email | [optional] 
 **application_name** | **str**| If specified, filters by application name | [optional] 
 **first_name** | **str**| If specified, filters by application first_name | [optional] 
 **last_name** | **str**| If specified, filters by application last_name | [optional] 
 **application_type** | [**ApplicationTypes**](.md)| If specified, filters by application application_type | [optional] 
 **created_after** | **datetime**| If specified, keeps only applications created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only applications created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **dedicated_workers** | **bool**| If specified, filters by dedicated_workers value | [optional] 
 **offset** | **int**| Number of the first document to send (pagination) | [optional] 
 **limit** | **int**| Maximum number of documents to send (pagination) | [optional] 
 **sort** | **str**| If specified, sorts the applications by a list of existing parameters separated by commas. Can be &#x27;application_name&#x27;, &#x27;application_type&#x27;, &#x27;creation_time&#x27;, &#x27;first_name&#x27;, &#x27;last_name&#x27;, &#x27;email&#x27;, &#x27;dedicated_workers&#x27;. Sorts in ascending order by default. If a parameter is preceded by &#x27;-&#x27;, it is sorted in descending order. | [optional] 

### Return type

[**list[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_reset_api_key**
> Application admin_reset_api_key(token, application_id)

Resets an API key (admin only)

Resets the API key of the application corresponding to application_id, and returns a new one. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ApplicationAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The id of the application to reset

try:
    # Resets an API key (admin only)
    api_response = api_instance.admin_reset_api_key(token, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationAdminApi->admin_reset_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The id of the application to reset | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

