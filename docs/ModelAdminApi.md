# leiaapi.generated.ModelAdminApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_apply_model_async**](ModelAdminApi.md#admin_apply_model_async) | **POST** /admin/{application_id}/model/{model_id}/apply/{document_ids} | Asynchronously applies a model on documents (admin only)
[**admin_create_model**](ModelAdminApi.md#admin_create_model) | **POST** /admin/{application_id}/model | Adds a new model to the system (admin only)
[**admin_delete_model**](ModelAdminApi.md#admin_delete_model) | **DELETE** /admin/{application_id}/model/{model_id} | Deletes a model (admin only)
[**admin_edit_model**](ModelAdminApi.md#admin_edit_model) | **PATCH** /admin/{application_id}/model/{model_id} | Modifies an existing model in the system (admin only)
[**admin_get_model**](ModelAdminApi.md#admin_get_model) | **GET** /admin/{application_id}/model/{model_id} | Get a model (admin only)
[**admin_get_model_contents**](ModelAdminApi.md#admin_get_model_contents) | **GET** /admin/{application_id}/model/{model_id}/file_contents | Get a model (admin only)
[**admin_get_models**](ModelAdminApi.md#admin_get_models) | **GET** /admin/model | Lists models (admin only) (paginated))
[**admin_tag_model**](ModelAdminApi.md#admin_tag_model) | **POST** /admin/{application_id}/model/{model_id}/tag/{tag} | Tags a model (admin only)
[**admin_train_model_async**](ModelAdminApi.md#admin_train_model_async) | **POST** /admin/{application_id}/model/{model_module}/train/{documents_tag} | Asynchronously trains a model on documents (admin only)
[**admin_untag_model**](ModelAdminApi.md#admin_untag_model) | **DELETE** /admin/{application_id}/model/{model_id}/tag/{tag} | Untags a model (admin only)

# **admin_apply_model_async**
> Job admin_apply_model_async(token, application_id, model_id, document_ids, body=body, tag=tag, format_type=format_type, execute_after_id=execute_after_id, page_range=page_range, callback_url=callback_url, model_params=model_params, block_processing=block_processing)

Asynchronously applies a model on documents (admin only)

Asynchronously applies an accessible model on accessible documents and returns a Job, that will have to be polled to get the result. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model belongs
model_id = 'model_id_example' # str | The id or the short name of the model to apply on the document
document_ids = ['document_ids_example'] # list[str] | Comma separated list of document ids to process
body = leiaapi.generated.ApplyBody() # ApplyBody | All the previous query parameters can also be passed as JSON in the body of the request (optional)
tag = 'tag_example' # str | The tag of the documents to process. If tag is present, document_ids should contain a single value, and the documents processed will be those where original_id=document_ids[0] and that contain the specified tag (optional)
format_type = leiaapi.generated.FormatTypes() # FormatTypes | The format in which the data should be returned. If empty, will return an array of key-value items. If it is classification, the result will be a Classification object. (optional)
execute_after_id = 'execute_after_id_example' # str | The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail (optional)
page_range = 'page_range_example' # str | The pages that should be used in previous job to process this one. Can only be used if execute_after_id is not null. Pages are indexed from 0. Syntax is the same as Python slices syntax (https://docs.python.org/3/whatsnew/2.3.html#extended-slices). Examples :   * Single positive integer : keep only this page (example 4 will keep only page 5 (Remember, pages are indexed from 0))   * Single negative integer : keep only this page, but starting from the end (example -4 will keep only page 7 if there are 10 total pages)   * Range (x:y) : keep only this range of pages (Including x but excluding y, indexed from 0)     Examples       * 2: will keep all pages starting from page 3       * :5 will keep only pages 1 to 5       * 2:5 will keep only pages 3, 4 and 5       * -4: will keep only pages 7 to 10 if there are 10 total pages)       * :-2 will keep only pages 1 to 8 if there are 10 total pages)       * -4:-2 will keep only pages 7 and 8 if there are 10 total pages)   * Stride (::w) : Keep 1 page every w pages starting at the first one (example 2 will keep only odd pages)   * Range and stride (x:y:w) : Keep 1 page every w pages within range (x:y) (example 1::2 will keep only even pages) You can use multiple ranges of page at once, comma separated (For example, 0,2:5,-2:-1 keeps the 1st page, plus pages 3->5, plus the second to last page)  (optional)
callback_url = 'callback_url_example' # str | Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. (optional)
model_params = NULL # object | Additional parameters that will be passed as is to the model (optional)
block_processing = true # bool | If true, blocks processing on the job until /job/{id}/start is called. Default is false (optional)

try:
    # Asynchronously applies a model on documents (admin only)
    api_response = api_instance.admin_apply_model_async(token, application_id, model_id, document_ids, body=body, tag=tag, format_type=format_type, execute_after_id=execute_after_id, page_range=page_range, callback_url=callback_url, model_params=model_params, block_processing=block_processing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_apply_model_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model belongs | 
 **model_id** | **str**| The id or the short name of the model to apply on the document | 
 **document_ids** | [**list[str]**](str.md)| Comma separated list of document ids to process | 
 **body** | [**ApplyBody**](ApplyBody.md)| All the previous query parameters can also be passed as JSON in the body of the request | [optional] 
 **tag** | **str**| The tag of the documents to process. If tag is present, document_ids should contain a single value, and the documents processed will be those where original_id&#x3D;document_ids[0] and that contain the specified tag | [optional] 
 **format_type** | [**FormatTypes**](.md)| The format in which the data should be returned. If empty, will return an array of key-value items. If it is classification, the result will be a Classification object. | [optional] 
 **execute_after_id** | **str**| The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail | [optional] 
 **page_range** | **str**| The pages that should be used in previous job to process this one. Can only be used if execute_after_id is not null. Pages are indexed from 0. Syntax is the same as Python slices syntax (https://docs.python.org/3/whatsnew/2.3.html#extended-slices). Examples :   * Single positive integer : keep only this page (example 4 will keep only page 5 (Remember, pages are indexed from 0))   * Single negative integer : keep only this page, but starting from the end (example -4 will keep only page 7 if there are 10 total pages)   * Range (x:y) : keep only this range of pages (Including x but excluding y, indexed from 0)     Examples       * 2: will keep all pages starting from page 3       * :5 will keep only pages 1 to 5       * 2:5 will keep only pages 3, 4 and 5       * -4: will keep only pages 7 to 10 if there are 10 total pages)       * :-2 will keep only pages 1 to 8 if there are 10 total pages)       * -4:-2 will keep only pages 7 and 8 if there are 10 total pages)   * Stride (::w) : Keep 1 page every w pages starting at the first one (example 2 will keep only odd pages)   * Range and stride (x:y:w) : Keep 1 page every w pages within range (x:y) (example 1::2 will keep only even pages) You can use multiple ranges of page at once, comma separated (For example, 0,2:5,-2:-1 keeps the 1st page, plus pages 3-&gt;5, plus the second to last page)  | [optional] 
 **callback_url** | **str**| Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. | [optional] 
 **model_params** | [**object**](.md)| Additional parameters that will be passed as is to the model | [optional] 
 **block_processing** | **bool**| If true, blocks processing on the job until /job/{id}/start is called. Default is false | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_model**
> Model admin_create_model(body, token, name, application_id, short_name=short_name, description=description, ttl=ttl, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, tags=tags)

Adds a new model to the system (admin only)

Adds a new model to the system and prepares structures to be able to serve it. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
body = leiaapi.generated.Object() # Object | 
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
name = 'name_example' # str | The name of the model
application_id = 'application_id_example' # str | The application that will own the model
short_name = 'short_name_example' # str | The new short name of the model (optional)
description = 'description_example' # str | The description of the model (optional)
ttl = 56 # int | The TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) (optional)
allowed_application_ids = ['allowed_application_ids_example'] # list[str] | The applications allowed to use this model (optional)
allow_all_applications = true # bool | Is this model allowed for everyone ? (optional)
tags = ['tags_example'] # list[str] | The tags of the model (optional)

try:
    # Adds a new model to the system (admin only)
    api_response = api_instance.admin_create_model(body, token, name, application_id, short_name=short_name, description=description, ttl=ttl, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  | 
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **name** | **str**| The name of the model | 
 **application_id** | **str**| The application that will own the model | 
 **short_name** | **str**| The new short name of the model | [optional] 
 **description** | **str**| The description of the model | [optional] 
 **ttl** | **int**| The TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) | [optional] 
 **allowed_application_ids** | [**list[str]**](str.md)| The applications allowed to use this model | [optional] 
 **allow_all_applications** | **bool**| Is this model allowed for everyone ? | [optional] 
 **tags** | [**list[str]**](str.md)| The tags of the model | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_model**
> admin_delete_model(token, application_id, model_id)

Deletes a model (admin only)

Get a model in the system that the application can access. This method is only accessible to admins. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to delete belongs
model_id = 'model_id_example' # str | The id of the model to delete

try:
    # Deletes a model (admin only)
    api_instance.admin_delete_model(token, application_id, model_id)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to delete belongs | 
 **model_id** | **str**| The id of the model to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_edit_model**
> Model admin_edit_model(token, application_id, model_id, name=name, short_name=short_name, description=description, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, ttl=ttl)

Modifies an existing model in the system (admin only)

Modifies a model already in the system. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to modify belongs
model_id = 'model_id_example' # str | The id of the model
name = 'name_example' # str | The new name of the model (optional)
short_name = 'short_name_example' # str | The new short name of the model (optional)
description = 'description_example' # str | The new description of the model (optional)
allowed_application_ids = ['allowed_application_ids_example'] # list[str] | The applications allowed to use this model. Clears the list if empty (optional)
allow_all_applications = true # bool | Is this model allowed for everyone ? (optional)
ttl = 56 # int | The new TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) (optional)

try:
    # Modifies an existing model in the system (admin only)
    api_response = api_instance.admin_edit_model(token, application_id, model_id, name=name, short_name=short_name, description=description, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, ttl=ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_edit_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to modify belongs | 
 **model_id** | **str**| The id of the model | 
 **name** | **str**| The new name of the model | [optional] 
 **short_name** | **str**| The new short name of the model | [optional] 
 **description** | **str**| The new description of the model | [optional] 
 **allowed_application_ids** | [**list[str]**](str.md)| The applications allowed to use this model. Clears the list if empty | [optional] 
 **allow_all_applications** | **bool**| Is this model allowed for everyone ? | [optional] 
 **ttl** | **int**| The new TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_model**
> Model admin_get_model(token, application_id, model_id)

Get a model (admin only)

Get a model in the system that the application can access. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to retrieve belongs
model_id = 'model_id_example' # str | The id or the short name of the model to get

try:
    # Get a model (admin only)
    api_response = api_instance.admin_get_model(token, application_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to retrieve belongs | 
 **model_id** | **str**| The id or the short name of the model to get | 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_model_contents**
> str admin_get_model_contents(token, application_id, model_id)

Get a model (admin only)

Get a model in the system that the application can access. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to retrieve belongs
model_id = 'model_id_example' # str | The id or the short name of the model to get

try:
    # Get a model (admin only)
    api_response = api_instance.admin_get_model_contents(token, application_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_get_model_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to retrieve belongs | 
 **model_id** | **str**| The id or the short name of the model to get | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_models**
> list[Model] admin_get_models(token, model_id=model_id, application_id=application_id, model_type=model_type, name=name, short_name=short_name, description=description, input_types=input_types, tags=tags, created_after=created_after, created_before=created_before, only_mine=only_mine, sort=sort, offset=offset, limit=limit)

Lists models (admin only) (paginated))

Lists all models. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
model_id = 'model_id_example' # str | The id of the models (optional)
application_id = 'application_id_example' # str | The application that owns the models (optional)
model_type = leiaapi.generated.ModelTypes() # ModelTypes | Filter by type (optional)
name = 'name_example' # str | Filter by name (optional)
short_name = 'short_name_example' # str | Filter by short name (optional)
description = 'description_example' # str | Gets models that contain this string in their description (optional)
input_types = [leiaapi.generated.ModelInputTypes()] # list[ModelInputTypes] | Filter by input type (optional)
tags = ['tags_example'] # list[str] | If specified, filters the models by tag (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only models created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only models created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
only_mine = true # bool | If true, will list only models that strictly belong to application_id if present, or to connected application else (and not all the models that it can use) (false by default) (optional)
sort = 'sort_example' # str | If specified, sorts the models by a list of existing parameters separated by commas. Can be 'application_id', 'creation_time', 'name', 'description', 'model_type'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order. (optional)
offset = 56 # int | Number of the first model to send (pagination) (optional)
limit = 56 # int | Maximum number of models to send (pagination) (optional)

try:
    # Lists models (admin only) (paginated))
    api_response = api_instance.admin_get_models(token, model_id=model_id, application_id=application_id, model_type=model_type, name=name, short_name=short_name, description=description, input_types=input_types, tags=tags, created_after=created_after, created_before=created_before, only_mine=only_mine, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **model_id** | **str**| The id of the models | [optional] 
 **application_id** | **str**| The application that owns the models | [optional] 
 **model_type** | [**ModelTypes**](.md)| Filter by type | [optional] 
 **name** | **str**| Filter by name | [optional] 
 **short_name** | **str**| Filter by short name | [optional] 
 **description** | **str**| Gets models that contain this string in their description | [optional] 
 **input_types** | [**list[ModelInputTypes]**](ModelInputTypes.md)| Filter by input type | [optional] 
 **tags** | [**list[str]**](str.md)| If specified, filters the models by tag | [optional] 
 **created_after** | **datetime**| If specified, keeps only models created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only models created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **only_mine** | **bool**| If true, will list only models that strictly belong to application_id if present, or to connected application else (and not all the models that it can use) (false by default) | [optional] 
 **sort** | **str**| If specified, sorts the models by a list of existing parameters separated by commas. Can be &#x27;application_id&#x27;, &#x27;creation_time&#x27;, &#x27;name&#x27;, &#x27;description&#x27;, &#x27;model_type&#x27;. Sorts in ascending order by default. If a parameter is preceded by &#x27;-&#x27;, it is sorted in descending order. | [optional] 
 **offset** | **int**| Number of the first model to send (pagination) | [optional] 
 **limit** | **int**| Maximum number of models to send (pagination) | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_tag_model**
> Model admin_tag_model(token, application_id, model_id, tag)

Tags a model (admin only)

Tags a model. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to tag belongs
model_id = 'model_id_example' # str | The id of the model
tag = 'tag_example' # str | The tag to add to the model

try:
    # Tags a model (admin only)
    api_response = api_instance.admin_tag_model(token, application_id, model_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_tag_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to tag belongs | 
 **model_id** | **str**| The id of the model | 
 **tag** | **str**| The tag to add to the model | 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_train_model_async**
> Job admin_train_model_async(token, application_id, model_module, documents_tag, body=body, model_name=model_name, short_name=short_name, description=description, ttl=ttl, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, tags=tags, execute_after_id=execute_after_id, callback_url=callback_url, model_params=model_params)

Asynchronously trains a model on documents (admin only)

Asynchronously trains a model on accessible documents and returns a Job, that will have to be polled to get the model. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model belongs
model_module = 'model_module_example' # str | The module name of the model to train on documents
documents_tag = 'documents_tag_example' # str | The tag of the documents to train with
body = leiaapi.generated.TrainBody() # TrainBody | All the previous query parameters can also be passed as JSON in the body of the request (optional)
model_name = 'model_name_example' # str | The future name of the model in database (optional)
short_name = 'short_name_example' # str | The new short name of the model (optional)
description = 'description_example' # str | The description of the model (optional)
ttl = 56 # int | The TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) (optional)
allowed_application_ids = ['allowed_application_ids_example'] # list[str] | The applications allowed to use this model (optional)
allow_all_applications = true # bool | Is this model allowed for everyone ? (optional)
tags = ['tags_example'] # list[str] | The tags of the model (optional)
execute_after_id = 'execute_after_id_example' # str | The job that is a prerequisite for this job to run (optional)
callback_url = 'callback_url_example' # str | Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. (optional)
model_params = NULL # object | Additional parameters that will be passed as is to the train method (optional)

try:
    # Asynchronously trains a model on documents (admin only)
    api_response = api_instance.admin_train_model_async(token, application_id, model_module, documents_tag, body=body, model_name=model_name, short_name=short_name, description=description, ttl=ttl, allowed_application_ids=allowed_application_ids, allow_all_applications=allow_all_applications, tags=tags, execute_after_id=execute_after_id, callback_url=callback_url, model_params=model_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_train_model_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model belongs | 
 **model_module** | **str**| The module name of the model to train on documents | 
 **documents_tag** | **str**| The tag of the documents to train with | 
 **body** | [**TrainBody**](TrainBody.md)| All the previous query parameters can also be passed as JSON in the body of the request | [optional] 
 **model_name** | **str**| The future name of the model in database | [optional] 
 **short_name** | **str**| The new short name of the model | [optional] 
 **description** | **str**| The description of the model | [optional] 
 **ttl** | **int**| The TTL of the model in seconds, if running in worker mode (negative for infinite TTL, default is 200) | [optional] 
 **allowed_application_ids** | [**list[str]**](str.md)| The applications allowed to use this model | [optional] 
 **allow_all_applications** | **bool**| Is this model allowed for everyone ? | [optional] 
 **tags** | [**list[str]**](str.md)| The tags of the model | [optional] 
 **execute_after_id** | **str**| The job that is a prerequisite for this job to run | [optional] 
 **callback_url** | **str**| Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. | [optional] 
 **model_params** | [**object**](.md)| Additional parameters that will be passed as is to the train method | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_untag_model**
> admin_untag_model(token, application_id, model_id, tag)

Untags a model (admin only)

Untags a model. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.ModelAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the model to untag belongs
model_id = 'model_id_example' # str | The id of the model
tag = 'tag_example' # str | The tag to delete from the model

try:
    # Untags a model (admin only)
    api_instance.admin_untag_model(token, application_id, model_id, tag)
except ApiException as e:
    print("Exception when calling ModelAdminApi->admin_untag_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the model to untag belongs | 
 **model_id** | **str**| The id of the model | 
 **tag** | **str**| The tag to delete from the model | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

