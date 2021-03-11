# leiaapi/generated.DocumentAdminApi

All URIs are relative to *https://api.leia.io/leia/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_create_document**](DocumentAdminApi.md#admin_create_document) | **POST** /admin/{application_id}/document | Uploads a document to the Leia API (admin only)
[**admin_delete_document**](DocumentAdminApi.md#admin_delete_document) | **DELETE** /admin/{application_id}/document/{document_id} | Deletes a document from Leia API (admin only)
[**admin_edit_document**](DocumentAdminApi.md#admin_edit_document) | **PATCH** /admin/{application_id}/document/{document_id} | Updates a document in Leia API (admin only)
[**admin_get_document**](DocumentAdminApi.md#admin_get_document) | **GET** /admin/{application_id}/document/{document_id} | Retrieves a document from Leia API (admin only)
[**admin_get_document_contents**](DocumentAdminApi.md#admin_get_document_contents) | **GET** /admin/{application_id}/document/{document_id}/file_contents | Retrieves a document from Leia API (admin only)
[**admin_get_documents**](DocumentAdminApi.md#admin_get_documents) | **GET** /admin/document | Retrieves documents from Leia API (admin only) (paginated)
[**admin_get_documents_tags**](DocumentAdminApi.md#admin_get_documents_tags) | **GET** /admin/document/tag | Retrieves documents&#x27; tags from Leia API (admin only)
[**admin_get_documents_zip**](DocumentAdminApi.md#admin_get_documents_zip) | **GET** /admin/document/zip | Retrieves documents from Leia API (admin only) (paginated)
[**admin_tag_document**](DocumentAdminApi.md#admin_tag_document) | **POST** /admin/{application_id}/document/{document_id}/tag/{tag} | Tags a document (admin only)
[**admin_transform_document_async**](DocumentAdminApi.md#admin_transform_document_async) | **POST** /admin/{application_id}/document/{document_ids}/transform/{output_type} | Asynchronously converts a document within Leia API (admin only)
[**admin_untag_document**](DocumentAdminApi.md#admin_untag_document) | **DELETE** /admin/{application_id}/document/{document_id}/tag/{tag} | Untags an document (admin only)

# **admin_create_document**
> Document admin_create_document(body, token, filename, application_id, ttl=ttl, tags=tags)

Uploads a document to the Leia API (admin only)

Uploads a document to Leia API for future use. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
body = leiaapi/generated.Object() # Object | 
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
filename = 'filename_example' # str | The name of the file (if present, extension will be separated from filename in metadata of the document)
application_id = 'application_id_example' # str | The application that will own the model
ttl = 56 # int | The TTL (in seconds, not less than 60) for the document (if present, the document and any sub documents, annotations, or jobs linked to it will be deleted after the TTL is expired) (optional)
tags = ['tags_example'] # list[str] | The tags of the document (optional)

try:
    # Uploads a document to the Leia API (admin only)
    api_response = api_instance.admin_create_document(body, token, filename, application_id, ttl=ttl, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  | 
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **filename** | **str**| The name of the file (if present, extension will be separated from filename in metadata of the document) | 
 **application_id** | **str**| The application that will own the model | 
 **ttl** | **int**| The TTL (in seconds, not less than 60) for the document (if present, the document and any sub documents, annotations, or jobs linked to it will be deleted after the TTL is expired) | [optional] 
 **tags** | [**list[str]**](str.md)| The tags of the document | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_document**
> admin_delete_document(token, application_id, document_id)

Deletes a document from Leia API (admin only)

Deletes a document from Leia API. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to delete belongs
document_id = 'document_id_example' # str | The id of the document to delete

try:
    # Deletes a document from Leia API (admin only)
    api_instance.admin_delete_document(token, application_id, document_id)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to delete belongs | 
 **document_id** | **str**| The id of the document to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_edit_document**
> Document admin_edit_document(token, application_id, document_id, filename=filename, rotation_angle=rotation_angle, ttl=ttl)

Updates a document in Leia API (admin only)

Updates metadata for a document. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to update belongs
document_id = 'document_id_example' # str | The id of the document to update
filename = 'filename_example' # str | The new file name of the document (optional)
rotation_angle = 56 # int | The new rotation angle of the document (optional)
ttl = 56 # int | The TTL (in seconds, not less than 60) for the document (if present, the document and any sub documents, annotations, or jobs linked to it will be deleted after the TTL is expired) (optional)

try:
    # Updates a document in Leia API (admin only)
    api_response = api_instance.admin_edit_document(token, application_id, document_id, filename=filename, rotation_angle=rotation_angle, ttl=ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_edit_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to update belongs | 
 **document_id** | **str**| The id of the document to update | 
 **filename** | **str**| The new file name of the document | [optional] 
 **rotation_angle** | **int**| The new rotation angle of the document | [optional] 
 **ttl** | **int**| The TTL (in seconds, not less than 60) for the document (if present, the document and any sub documents, annotations, or jobs linked to it will be deleted after the TTL is expired) | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_document**
> Document admin_get_document(token, application_id, document_id)

Retrieves a document from Leia API (admin only)

Retrieves a document from Leia API as metadata. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to retrieve belongs
document_id = 'document_id_example' # str | The id of the document to retrieve

try:
    # Retrieves a document from Leia API (admin only)
    api_response = api_instance.admin_get_document(token, application_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to retrieve belongs | 
 **document_id** | **str**| The id of the document to retrieve | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_document_contents**
> str admin_get_document_contents(token, application_id, document_id, max_size=max_size, jpeg_compression=jpeg_compression)

Retrieves a document from Leia API (admin only)

Retrieves the binary contents of a document from Leia API. This method is only accessible to admins 

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to retrieve belongs
document_id = 'document_id_example' # str | The id of the document to retrieve
max_size = 56 # int | Restrict the size of the image to get (only applicable for documents of type image). The largest dimension of the image will be capped to this dimension (optional)
jpeg_compression = 56 # int | JPEG compression rate, in percent (only applicable for documents of type image) (optional)

try:
    # Retrieves a document from Leia API (admin only)
    api_response = api_instance.admin_get_document_contents(token, application_id, document_id, max_size=max_size, jpeg_compression=jpeg_compression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_get_document_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to retrieve belongs | 
 **document_id** | **str**| The id of the document to retrieve | 
 **max_size** | **int**| Restrict the size of the image to get (only applicable for documents of type image). The largest dimension of the image will be capped to this dimension | [optional] 
 **jpeg_compression** | **int**| JPEG compression rate, in percent (only applicable for documents of type image) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_documents**
> list[Document] admin_get_documents(token, document_id=document_id, application_id=application_id, filename=filename, extension=extension, mime_type=mime_type, original_id=original_id, tags=tags, created_after=created_after, created_before=created_before, tag_result=tag_result, sort=sort, offset=offset, limit=limit)

Retrieves documents from Leia API (admin only) (paginated)

Retrieves documents which matches the query from Leia API as JSON metadata. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
document_id = 'document_id_example' # str | The id of the document (optional)
application_id = 'application_id_example' # str | The application that owns the documents (optional)
filename = 'filename_example' # str | The file name of the documents to retrieve (optional)
extension = 'extension_example' # str | The extension of the documents to retrieve (optional)
mime_type = 'mime_type_example' # str | Filters by MIME type (optional)
original_id = 'original_id_example' # str | Filters by original id (optional)
tags = ['tags_example'] # list[str] | If specified, filters the documents by tag (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only documents created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only documents created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
tag_result = 'tag_result_example' # str | Atomically adds a tag to all retrieved values if specified. The added tag will not be returned in the result (optional)
sort = 'sort_example' # str | If specified, sorts the documents by a list of existing parameters separated by commas. Can be 'application_id', 'filename', 'extension', 'mime_type', 'original_id', 'page', 'creation_time'. Sorts in ascending order by default. If a parameter is preceded by '-', it is sorted in descending order. (optional)
offset = 56 # int | Number of the first document to send (pagination) (optional)
limit = 56 # int | Maximum number of documents to send (pagination) (optional)

try:
    # Retrieves documents from Leia API (admin only) (paginated)
    api_response = api_instance.admin_get_documents(token, document_id=document_id, application_id=application_id, filename=filename, extension=extension, mime_type=mime_type, original_id=original_id, tags=tags, created_after=created_after, created_before=created_before, tag_result=tag_result, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **document_id** | **str**| The id of the document | [optional] 
 **application_id** | **str**| The application that owns the documents | [optional] 
 **filename** | **str**| The file name of the documents to retrieve | [optional] 
 **extension** | **str**| The extension of the documents to retrieve | [optional] 
 **mime_type** | **str**| Filters by MIME type | [optional] 
 **original_id** | **str**| Filters by original id | [optional] 
 **tags** | [**list[str]**](str.md)| If specified, filters the documents by tag | [optional] 
 **created_after** | **datetime**| If specified, keeps only documents created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only documents created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **tag_result** | **str**| Atomically adds a tag to all retrieved values if specified. The added tag will not be returned in the result | [optional] 
 **sort** | **str**| If specified, sorts the documents by a list of existing parameters separated by commas. Can be &#x27;application_id&#x27;, &#x27;filename&#x27;, &#x27;extension&#x27;, &#x27;mime_type&#x27;, &#x27;original_id&#x27;, &#x27;page&#x27;, &#x27;creation_time&#x27;. Sorts in ascending order by default. If a parameter is preceded by &#x27;-&#x27;, it is sorted in descending order. | [optional] 
 **offset** | **int**| Number of the first document to send (pagination) | [optional] 
 **limit** | **int**| Maximum number of documents to send (pagination) | [optional] 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_documents_tags**
> list[str] admin_get_documents_tags(token, application_id=application_id)

Retrieves documents' tags from Leia API (admin only)

Retrieves tags from documents. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | Restrict to tags belonging to this application (optional)

try:
    # Retrieves documents' tags from Leia API (admin only)
    api_response = api_instance.admin_get_documents_tags(token, application_id=application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_get_documents_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| Restrict to tags belonging to this application | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_documents_zip**
> str admin_get_documents_zip(token, document_id=document_id, application_id=application_id, filename=filename, extension=extension, mime_type=mime_type, original_id=original_id, tags=tags, created_after=created_after, created_before=created_before)

Retrieves documents from Leia API (admin only) (paginated)

Retrieves documents which matches the query from Leia API in a zip file. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
document_id = 'document_id_example' # str | The id of the document (optional)
application_id = 'application_id_example' # str | The application that owns the documents (optional)
filename = 'filename_example' # str | The file name of the documents to retrieve (optional)
extension = 'extension_example' # str | The extension of the documents to retrieve (optional)
mime_type = 'mime_type_example' # str | Filters by MIME type (optional)
original_id = 'original_id_example' # str | Filters by original id (optional)
tags = ['tags_example'] # list[str] | If specified, filters the documents by tag (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only documents created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If specified, keeps only documents created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) (optional)

try:
    # Retrieves documents from Leia API (admin only) (paginated)
    api_response = api_instance.admin_get_documents_zip(token, document_id=document_id, application_id=application_id, filename=filename, extension=extension, mime_type=mime_type, original_id=original_id, tags=tags, created_after=created_after, created_before=created_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_get_documents_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **document_id** | **str**| The id of the document | [optional] 
 **application_id** | **str**| The application that owns the documents | [optional] 
 **filename** | **str**| The file name of the documents to retrieve | [optional] 
 **extension** | **str**| The extension of the documents to retrieve | [optional] 
 **mime_type** | **str**| Filters by MIME type | [optional] 
 **original_id** | **str**| Filters by original id | [optional] 
 **tags** | [**list[str]**](str.md)| If specified, filters the documents by tag | [optional] 
 **created_after** | **datetime**| If specified, keeps only documents created after given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 
 **created_before** | **datetime**| If specified, keeps only documents created before given UTC timestamp (ISO 8601 format : yyyy-MM-ddThh:mm:ss) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_tag_document**
> Document admin_tag_document(token, application_id, document_id, tag)

Tags a document (admin only)

Tags a document. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to tag belongs
document_id = 'document_id_example' # str | The id of the document
tag = 'tag_example' # str | The tag to add to the document

try:
    # Tags a document (admin only)
    api_response = api_instance.admin_tag_document(token, application_id, document_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_tag_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to tag belongs | 
 **document_id** | **str**| The id of the document | 
 **tag** | **str**| The tag to add to the document | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_transform_document_async**
> Job admin_transform_document_async(token, application_id, document_ids, output_type, body=body, input_tag=input_tag, output_tag=output_tag, execute_after_id=execute_after_id, page_range=page_range, callback_url=callback_url, transform_params=transform_params)

Asynchronously converts a document within Leia API (admin only)

Asynchronously transforms a document from its current type to the output_type. May generate multiple new documents (for example converting a PDF to image will generate one new image document for each page of the PDF). Returns a Job, that will have to be polled to get the result. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application id whose documents to transform belong to
document_ids = ['document_ids_example'] # list[str] | Comma separated list of document ids to process
output_type = leiaapi/generated.TransformTypes() # TransformTypes | The output type. May be:   * image (extract one image for each page in a PDF file)   * text (Use OCR on an image to get convert it to text)     * To use Google Vision OCR instead of normal LEIA OCR, add \"use_google_vision\":true in transform_params   * text_tree (text in the form of a JSON tree with information about text blocks and their position in the document)     * To use Google Vision OCR instead of normal LEIA OCR, add \"use_google_vision\":true in transform_params   * autorotate (Rotates an image that contains text so that it is in readable orientation)   * trim (Trims white space around a document)   * merge (Merge multiple text documents into a single one with a carriage return '\\n' between them)   * split (Splits a text document into chunks of 1000 words and replaces all spacing characters by single spaces (this number can be changed by setting split_size to another value in transform_params)) 
body = leiaapi/generated.TransformBody() # TransformBody | All the previous query parameters can also be passed as JSON in the body of the request (optional)
input_tag = 'input_tag_example' # str | The tag of the documents to process. If tag is present, document_ids should contain a single value, and the documents processed will be those where original_id=document_ids[0] and that contain the specified tag (optional)
output_tag = 'output_tag_example' # str | The tag to add to the documents resulting from the transformation (optional)
execute_after_id = 'execute_after_id_example' # str | The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail (optional)
page_range = 'page_range_example' # str | The pages that should be used in previous job to process this one. Can only be used if execute_after_id is not null. Pages are indexed from 0. Syntax is the same as Python slices syntax (https://docs.python.org/3/whatsnew/2.3.html#extended-slices). Examples :   * Single positive integer : keep only this page (example 4 will keep only page 5 (Remember, pages are indexed from 0))   * Single negative integer : keep only this page, but starting from the end (example -4 will keep only page 7 if there are 10 total pages)   * Range (x:y) : keep only this range of pages (Including x but excluding y, indexed from 0)     Examples       * 2: will keep all pages starting from page 3       * :5 will keep only pages 1 to 5       * 2:5 will keep only pages 3, 4 and 5       * -4: will keep only pages 7 to 10 if there are 10 total pages)       * :-2 will keep only pages 1 to 8 if there are 10 total pages)       * -4:-2 will keep only pages 7 and 8 if there are 10 total pages)   * Stride (::w) : Keep 1 page every w pages starting at the first one (example ::2 will keep only odd pages)   * Range and stride (x:y:w) : Keep 1 page every w pages within range (x:y) (example 1::2 will keep only even pages) You can use multiple ranges of page at once, comma separated (For example, 0,2:5,-2:-1 keeps the 1st page, plus pages 3->5, plus the second to last page)  (optional)
callback_url = 'callback_url_example' # str | Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. (optional)
transform_params = NULL # object | Free form parameters for the transformation (optional)

try:
    # Asynchronously converts a document within Leia API (admin only)
    api_response = api_instance.admin_transform_document_async(token, application_id, document_ids, output_type, body=body, input_tag=input_tag, output_tag=output_tag, execute_after_id=execute_after_id, page_range=page_range, callback_url=callback_url, transform_params=transform_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_transform_document_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application id whose documents to transform belong to | 
 **document_ids** | [**list[str]**](str.md)| Comma separated list of document ids to process | 
 **output_type** | [**TransformTypes**](.md)| The output type. May be:   * image (extract one image for each page in a PDF file)   * text (Use OCR on an image to get convert it to text)     * To use Google Vision OCR instead of normal LEIA OCR, add \&quot;use_google_vision\&quot;:true in transform_params   * text_tree (text in the form of a JSON tree with information about text blocks and their position in the document)     * To use Google Vision OCR instead of normal LEIA OCR, add \&quot;use_google_vision\&quot;:true in transform_params   * autorotate (Rotates an image that contains text so that it is in readable orientation)   * trim (Trims white space around a document)   * merge (Merge multiple text documents into a single one with a carriage return &#x27;\\n&#x27; between them)   * split (Splits a text document into chunks of 1000 words and replaces all spacing characters by single spaces (this number can be changed by setting split_size to another value in transform_params))  | 
 **body** | [**TransformBody**](TransformBody.md)| All the previous query parameters can also be passed as JSON in the body of the request | [optional] 
 **input_tag** | **str**| The tag of the documents to process. If tag is present, document_ids should contain a single value, and the documents processed will be those where original_id&#x3D;document_ids[0] and that contain the specified tag | [optional] 
 **output_tag** | **str**| The tag to add to the documents resulting from the transformation | [optional] 
 **execute_after_id** | **str**| The id of a job that must be in PROCESSED status before this one can be started (used to chain jobs even before the first ones are terminated). If the referenced job becomes FAILED or is CANCELED, this one will fail | [optional] 
 **page_range** | **str**| The pages that should be used in previous job to process this one. Can only be used if execute_after_id is not null. Pages are indexed from 0. Syntax is the same as Python slices syntax (https://docs.python.org/3/whatsnew/2.3.html#extended-slices). Examples :   * Single positive integer : keep only this page (example 4 will keep only page 5 (Remember, pages are indexed from 0))   * Single negative integer : keep only this page, but starting from the end (example -4 will keep only page 7 if there are 10 total pages)   * Range (x:y) : keep only this range of pages (Including x but excluding y, indexed from 0)     Examples       * 2: will keep all pages starting from page 3       * :5 will keep only pages 1 to 5       * 2:5 will keep only pages 3, 4 and 5       * -4: will keep only pages 7 to 10 if there are 10 total pages)       * :-2 will keep only pages 1 to 8 if there are 10 total pages)       * -4:-2 will keep only pages 7 and 8 if there are 10 total pages)   * Stride (::w) : Keep 1 page every w pages starting at the first one (example ::2 will keep only odd pages)   * Range and stride (x:y:w) : Keep 1 page every w pages within range (x:y) (example 1::2 will keep only even pages) You can use multiple ranges of page at once, comma separated (For example, 0,2:5,-2:-1 keeps the 1st page, plus pages 3-&gt;5, plus the second to last page)  | [optional] 
 **callback_url** | **str**| Callback URL that should be called when the job becomes PROCESSED/FAILED/CANCELED. This URL will be called with a HTTP POST method, and the Job object as the payload. Callback server must answer with either a 200 or 204 HTTP response, to acknowledge the callback. Any other response code will be considered as a failure to call the callback. | [optional] 
 **transform_params** | [**object**](.md)| Free form parameters for the transformation | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_untag_document**
> admin_untag_document(token, application_id, document_id, tag)

Untags an document (admin only)

Untags a document. This method is only accessible to admins

### Example
```python
from __future__ import print_function
import time
import leiaapi/generated
from leiaapi/generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leiaapi/generated.DocumentAdminApi()
token = 'token_example' # str | The login token obtained via GET /login/{api_key}
application_id = 'application_id_example' # str | The application to which the document to untag belongs
document_id = 'document_id_example' # str | The id of the document
tag = 'tag_example' # str | The tag to delete from the document

try:
    # Untags an document (admin only)
    api_instance.admin_untag_document(token, application_id, document_id, tag)
except ApiException as e:
    print("Exception when calling DocumentAdminApi->admin_untag_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The login token obtained via GET /login/{api_key} | 
 **application_id** | **str**| The application to which the document to untag belongs | 
 **document_id** | **str**| The id of the document | 
 **tag** | **str**| The tag to delete from the document | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

