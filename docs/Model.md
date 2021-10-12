# Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_all_applications** | **bool** |  | [optional] 
**allowed_application_ids** | **list[str]** |  | [optional] 
**application_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | 
**description** | **str** |  | [optional] 
**documentation** | **str** |  | [optional] 
**id** | **str** |  | 
**input_types** | [**list[ModelInputTypes]**](ModelInputTypes.md) |  | 
**md5sum** | **str** | The MD5 sum of the model | [optional] 
**model_clazz** | **str** | The Python class name of the model | 
**model_module** | **str** | The Python module ghosting the code for the model | 
**model_type** | [**ModelTypes**](ModelTypes.md) |  | 
**name** | **str** |  | 
**output_format** | **object** |  | [optional] 
**short_name** | **str** |  | [optional] 
**size** | **float** |  | 
**speed** | [**Speed**](Speed.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**ttl** | **float** | The TTL of the workers hosting this model | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

