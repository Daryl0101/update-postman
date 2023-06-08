# Update Postman Collection
Imports the latest version of `swagger.json` and update the respective Postman collection using Python.

## To get things started:
1. Make sure you have [Python 3.10](https://www.python.org/downloads/release/python-3100/) & [npm](https://www.npmjs.com/) installed.
2. Pull this repo.
3. Create a `venv` virtual environment.
4. Install [openapi2postmanv2](https://github.com/postmanlabs/openapi-to-postman) globally using `$ npm i -g openapi-to-postmanv2` command to use it in the CLI. 
5. Install dependencies in `requirements.txt` file.
6. Edit your secrets in the `.env` file.
7. Add new environments in the `global_data.py` file. [optional]
8. Execute `main.py`.
