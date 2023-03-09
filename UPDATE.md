## Update the library
- Download [swagger-codegen](https://openapi-generator.tech/docs/installation)
- Be sure that you have a version equal or superior of 6.4.0 (ex: openapi-generator-cli-6.4.0.jar)
- Run the following command, replacing \<folderName\> by the name of the folder where the project is 
    ```shell<<<<
    java -jar .\openapi-generator-cli-6.4.0.jar generate --skip-validate-spec -g python-nextgen -o "~\LeiaApiSdk" -i "https://dev.leia.id360docaposte.com/leia/1.0.0/openapi.json" --additional-properties=packageName=leiaapi.generated
    ```
- If you set the output folder in the current project take caution of the file which will be overwritten (all files in leiaapi/generated + setup.py, README.md, ...)
- If you have used a different folder, copy everything from leiaapi.generated to the same folder in the project
- Modify `leiaapi.generated.models.model_input_types.ModelInputTypes` to include `LIST_PDF = 'list[pdf]'`
- Modify `leiaapi.generated.api.api_client.ApiClient.parameters_to_url_query` to add 
  ```python
  if isinstance(v, bool):
    v = str(v).lower()
  # add this
  if isinstance(v, dict):
    for l, b in v.items():
      new_params.append((l,b))
    continue
  ```
- Modify `leiaapi.generated.api.api_client.ApiClient.parameters_to_tuples` to add 
  ```python
  for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
    # Add this
    if isinstance(v, Enum):
      print(v)
      v = v.value
  ```
- Les tests `test_application_api` doivent fonctionner. Il est nécéssaire de modifier le code pour qu'ils fonctionnent. Exemples: 
  - la plupart des changement sont surtout pour certain retour qui sont en str au lieu de bytes
  - dans `actual_instance_must_validate_oneof` et `from_json` de `job_result` rajoutez `if match == 0:` au desus du bloc commencant par `# deserialize data into object`

## Deploy-
- Change version in setup.py
- `python3 -m pip install --upgrade build`
- `python3 -m pip install --user --upgrade twine`
- `python3 -m build`
- `python3 -m twine upload --repository pypi dist/*`
- For the field `Enter your username`, put `__token__`
- For the field `Enter your password`, put the token you have generated on the pypi platform