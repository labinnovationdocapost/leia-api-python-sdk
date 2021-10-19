## Update the library
- Download [swagger-codegen](https://github.com/swagger-api/swagger-codegen)
- Be sure that you have a version equal or superior of 3.* (ex: swagger-codegen-cli-3.0.25)
- Run the following command, replacing \<folderName\> by the name of the folder where the project is 
    ```shell<<<<
    java -jar .\swagger-codegen-cli-3.0.25.jar generate -l python -o <folderName> -i https://api.leia.io/leia/1.0.0/openapi.json -c <folderName>\config.json
    ```
- until version 1.0.25 `packageName` in `config.json` must be of the form `module1/module2/module3` which corrupt the output file, but make the folder hierarchy correct.
- To patch it replace all `leiaapi/generated` by `leiaapi.generated`  
  on pycharm use CTRL+SHIT+R to replace in the whole project, but make sure to not touch `config.json` or  
  If you are using git, you can roll back the file to its original state
- Take caution of the file which will be overwritten (all files in leiaapi/generated + setup.py, README.md, ...)
- [DEPRECATED] Replace every `collection_formats['document_ids'] = 'multi'` for `collection_formats['document_ids'] = ''`
- in `leiaapi.generated.api_client.py` around line 120 replace:
  ```python
  for k, v in valid_path_params:
  ```
  by
  ```python
  from itertools import groupby
  valid_path_params = []
  for k, g in groupby(path_params, key=lambda x: x[0]):
      valid_path_params.append((k, ",".join(list(map(lambda x: x[1], g)))))
  for k, v in valid_path_params:
  ```
- In `rest_api.py` function `request` modify
  ```python
  elif isinstance(body, str):
    request_body = body
    r = self.pool_manager.request(
      method, url,
      body=request_body,
      preload_content=_preload_content,
      timeout=timeout,
      headers=headers)
   ```
    by
  ```python
  elif isinstance(body, str) or isinstance(body, bytes):
    request_body = body
    r = self.pool_manager.request(
      method, url,
      body=request_body,
      preload_content=_preload_content,
      timeout=timeout,
      headers=headers)
   ```

## Deploy
- Change version in setup.py
- `python3 -m pip install --upgrade build`
- `python3 -m pip install --user --upgrade twine`
- `python3 -m build`
- `python3 -m twine upload --repository pypi dist/*`
- For the field `Enter your username`, put `__token__`
- For the field `Enter your password`, put the token you have generated on the pypi platform