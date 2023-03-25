# create venv folder

```bash
python -m venv venv
```

=> python : interpreter
=> -m: run module as a script
=> venv: name of module that creates virtual environment in python
=> venv: name of the folder

# create requirements.txt

(pip is a package manager for python)
(Python Package Index (PyPI) for python => similar to npm packages)

```bash
pip freeze > requirements.txt

```

# install requirements

```bash
pip install -r requirements.txt

```

# main.yaml (ci/cd)

```yaml
name: CI

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE
      - uses: actions/checkout@v2

      # Set up Python 3.11.2 environment
      - name: Set up Python 3.11.2
        uses: actions/setup-python@v1
        with:
          python-version: "3.11.2"

      # Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      # Run our unit tests
      - name: Run unit tests
        run: |
          python test_application.py
  deploy-to-test:
    # Only run this job if "build" has ended successfully
    needs:
      - build

    runs-on: ubuntu-latest

    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE
      - uses: actions/checkout@v2

      # Set up Python 3.8 environment
      - name: Set up Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: "3.8"

      # Set up cache for pip
      - name: Get pip cache dir
        id: pip-cache
        run: |
          echo "::set-output name=dir::$(pip cache dir)"
      - name: Cache pip
        uses: actions/cache@v1
        with:
          path: ${{ steps.pip-cache.outputs.dir }}
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      # Elastic Beanstalk CLI version
      - name: Get EB CLI version
        run: |
          python -m pip install --upgrade pip
          pip install awsebcli --upgrade
          eb --version
      # Configure AWS Credentials
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      # Create the Elastic Beanstalk application
      - name: Create EBS application
        run: |
          eb init -p python-3.7 hello-world --region us-east-1
      # Create the Elastic Beanstalk environment
      - name: Create test environment
        run: |
          eb create test-environment
```
