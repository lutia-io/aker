# Aker

<https://en.wikipedia.org/wiki/Aker_(deity)>

## Requirements

- Python 3.12.3
- Kind 0.24.0
- Skaffold 2.13.2

## Setup & Run

- Create a new main project folder anywhere you like
  - `mkdir aker-project`
  - `cd aker-project`
- Setup a virtual environment using the following command:
  - `python3.12 -m venv aker-env`
- Activate the virtual environment using the following command:
  - `source aker-env/bin/activate`
  - You should now see your terminal like:
    - `(aker-env) user:aker-project/ $`
- Clone this repository using git clone:
  - `git clone git@github.com:lutia-io/aker.git`
  - `cd aker`
- Create a new `skaffold.env` file and paste the bare minimum key/values needed. You can view all the available environment variables [here](docs/environment.md).

    ```bash
    AKER_DEBUG=true
    ```

- Install the library dependencies
  - `pip install -r requirements.txt`
- Release Lutia platform
  - `skaffold dev`

## Installing pip packages

- If you would like to use an external library; after installing it, please ensure to freeze it to `requirements.txt`
  - `pip freeze > requirements.txt`

## Tests

- Run the tests using Django:
  - `python manage.py test`
- Run the tests using `coverage`:
  - `coverage run manage.py test`
- If you want to see the coverage results in your terminal:
  - `coverage report -m`
- If you want to see the coverage results with red/green diff, you can open a browser tool:
  - `coverage html`
- Open the generated HTML file located in `htmlcov/index.html` in a browser with absolute path
