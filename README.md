# Aker

<https://en.wikipedia.org/wiki/Aker_(deity)>

## Requirements

- Python 3.12.3
- Kubernetes 1.31.0
- Kind 0.24.0
- Helm 3.15.4
- Skaffold 2.13.2

## Setup & Run

- Create a new main project folder anywhere you like
  - `mkdir aker-project`
  - `cd aker-project`
- Setup a virtual environment using the following command:
  - `python3 -m venv aker-env`
- Activate the virtual environment using the following command:
  - `source aker-env/bin/activate`
  - You should now see your terminal like:
    - `(aker-env) user:aker-project/ $`
- Clone this repository using git clone:
  - `git clone git@github.com:lutia-io/aker.git`
  - `cd aker`
- Create a new `skaffold.env` file and paste the bare minimum key/values needed (see `.env.example`). You can view all the available environment variables [here](docs/environment.md).

    ```bash
    AKER_DEBUG=true
    ```

- Install the library dependencies
  - `pip install -r requirements.txt`
- Release Lutia platform
  - `skaffold dev`

## Installing pip packages

- After installing an external package, please ensure to freeze the pinned package to `requirements.txt`
  - `pip freeze > requirements.txt`

## Tests

- Build image using skaffold
  - `skaffold build --file-output build-artifacts.json`
- Use built artifact (image) to execute tests
  - `skaffold test --build-artifacts=build-artifacts.json`
