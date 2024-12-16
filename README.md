# Aker

<https://en.wikipedia.org/wiki/Aker_(deity)>

## Requirements

- Python 3.12
- Docker

## Setup

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
- Create a new `.env` file and paste the bare minimum key/values needed. You can view all the available environment variables [here](docs/environment.md).

    ```
    #!/bin/bash
    AKER_DEBUG=true
    ```

- Install the library dependencies
  - `pip install -r requirements.txt`
- Run the service dependencies
  - `docker compose up -d`
- Execute the migrations & run the API
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py runserver`

Furthermore, after setting up your environment, please continue to setup your API with your App [here](docs/setup.md).

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

## Docker (locally)

- You need to build the docker image using the following command:
  - `docker build -t aker .`
- Run the newly created docker image
  - `docker run --env-file .env -p 8000:8000 -d aker:latest`
