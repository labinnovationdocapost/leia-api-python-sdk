# leiaapi.generated.AnnotationApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationApi.md#create_annotation) | **POST** /annotation/{document_id} | Creates an annotation
[**delete_annotation**](AnnotationApi.md#delete_annotation) | **DELETE** /annotation/{annotation_id} | Deletes an annotation
[**get_annotation**](AnnotationApi.md#get_annotation) | **GET** /annotation/{annotation_id} | Retrieves an annotation
[**get_annotations**](AnnotationApi.md#get_annotations) | **GET** /annotation | Retrieves annotations (paginated)
[**tag_annotation**](AnnotationApi.md#tag_annotation) | **POST** /annotation/{annotation_id}/tag/{tag} | Tags an annotation
[**untag_annotation**](AnnotationApi.md#untag_annotation) | **DELETE** /annotation/{annotation_id}/tag/{tag} | Untags an annotation
[**update_annotation**](AnnotationApi.md#update_annotation) | **PATCH** /annotation/{annotation_id} | Updates an annotation

# **create_annotation**
> Annotation create_annotation(body, token, annotation_type, document_id, name=name, tags=tags)

Creates an annotation

Creates an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
body = NULL # object | The prediction that should be associated to document in this annotation, in free form json
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_type = leiaapi.generated.AnnotationTypes() # AnnotationTypes | The type of the annotation
document_id = 'document_id_example' # str | The id of the document to annotate
name = 'name_example' # str | The name of the annotation (for information purposes only) (optional)
tags = ['tags_example'] # list[str] | The tags of the annotation (optional)

try:
    # Creates an annotation
    api_response = api_instance.create_annotation(body, token, annotation_type, document_id, name=name, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The prediction that should be associated to document in this annotation, in free form json | 
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_type** | [**AnnotationTypes**](.md)| The type of the annotation | 
 **document_id** | **str**| The id of the document to annotate | 
 **name** | **str**| The name of the annotation (for information purposes only) | [optional] 
 **tags** | [**list[str]**](str.md)| The tags of the annotation | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation**
> delete_annotation(token, annotation_id)

Deletes an annotation

Deletes an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | The id of the annotation (for information purposes only)

try:
    # Deletes an annotation
    api_instance.delete_annotation(token, annotation_id)
except ApiException as e:
    print("Exception when calling AnnotationApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| The id of the annotation (for information purposes only) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotation**
> Annotation get_annotation(token, annotation_id)

Retrieves an annotation

Retrieves an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | The id of the annotation (for information purposes only)

try:
    # Retrieves an annotation
    api_response = api_instance.get_annotation(token, annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationApi->get_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| The id of the annotation (for information purposes only) | 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotations**
> list[Annotation] get_annotations(token, annotation_id=annotation_id, annotation_type=annotation_type, name=name, tags=tags, document_id=document_id, created_after=created_after, created_before=created_before, offset=offset, limit=limit)

Retrieves annotations (paginated)

Retrieves annotations

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | If specified, filters the annotations id (optional)
annotation_type = leiaapi.generated.AnnotationTypes() # AnnotationTypes | If specified, filters the annotations by type (optional)
name = 'name_example' # str | If specified, filters the annotations by name (optional)
tags = ['tags_example'] # list[str] | If specified, filters the annotations by tag (optional)
document_id = 'document_id_example' # str | If specified, filters the annotations attached to a given document (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only annotations created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only annotations created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
offset = 56 # int | Number of the first annotation to send (pagination) (optional)
limit = 56 # int | Maximum number of annotation to send (pagination) (optional)

try:
    # Retrieves annotations (paginated)
    api_response = api_instance.get_annotations(token, annotation_id=annotation_id, annotation_type=annotation_type, name=name, tags=tags, document_id=document_id, created_after=created_after, created_before=created_before, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationApi->get_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| If specified, filters the annotations id | [optional] 
 **annotation_type** | [**AnnotationTypes**](.md)| If specified, filters the annotations by type | [optional] 
 **name** | **str**| If specified, filters the annotations by name | [optional] 
 **tags** | [**list[str]**](str.md)| If specified, filters the annotations by tag | [optional] 
 **document_id** | **str**| If specified, filters the annotations attached to a given document | [optional] 
 **created_after** | **datetime**| If specified, keeps only annotations created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only annotations created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **offset** | **int**| Number of the first annotation to send (pagination) | [optional] 
 **limit** | **int**| Maximum number of annotation to send (pagination) | [optional] 

### Return type

[**list[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_annotation**
> Annotation tag_annotation(token, annotation_id, tag)

Tags an annotation

Tags an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | The id of the annotation
tag = 'tag_example' # str | The tag to add to the annotation

try:
    # Tags an annotation
    api_response = api_instance.tag_annotation(token, annotation_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationApi->tag_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| The id of the annotation | 
 **tag** | **str**| The tag to add to the annotation | 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untag_annotation**
> untag_annotation(token, annotation_id, tag)

Untags an annotation

Untags an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | The id of the annotation
tag = 'tag_example' # str | The tag to delete from the annotation

try:
    # Untags an annotation
    api_instance.untag_annotation(token, annotation_id, tag)
except ApiException as e:
    print("Exception when calling AnnotationApi->untag_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| The id of the annotation | 
 **tag** | **str**| The tag to delete from the annotation | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> Annotation update_annotation(body, token, annotation_id, name=name)

Updates an annotation

Updates an annotation

### Example
```python
from __future__ import print_function
import time
import leiaapi.generated
from leiaapi.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi.generated.AnnotationApi()
body = NULL # object | The new prediction that should be associated to document in this annotation, in free form json
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
annotation_id = 'annotation_id_example' # str | The id of the annotation to modify
name = 'name_example' # str | The new name of the annotation (won't change if not set) (optional)

try:
    # Updates an annotation
    api_response = api_instance.update_annotation(body, token, annotation_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The new prediction that should be associated to document in this annotation, in free form json | 
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **annotation_id** | **str**| The id of the annotation to modify | 
 **name** | **str**| The new name of the annotation (won&#x27;t change if not set) | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

