# Python Virtual Enviornments

## Virtualenv

### Install

```bash
pip install virtualenv
```

### Start a Project

```bash
cd my_project/
```



## Pipenv

Before piping, pip was used for package management and virtualenv was used for virtual environments.

Pipenv combines these.

### Install

```bash
pip install pipenv
```



### Start a Project

```bash
mkdir my_project            # create a new project
cd my_project/              # enter the project
pipenv install requests     # use pipenv to install the requests library

tree
.
├── Pipfile           # Pipfile created,
└── Pipfile.lock      # Pipfile.lock created, 
```

#### Pipfile

Uses toml format. Is an editable file.

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"      # "*" as no version selected, can be modified

[dev-packages]

[requires]
python_version = "3.8"
```

#### Pipfile.lock

Generated file that has more detail about the current environment.
Contains package and dependencies of libraries installed.
Don't manually modify this file.

#### Activate Enviornment

```
pipenv shell
```

Can see what python is being used now that we are in the pipenv shell

```python
python
>>> import sys
>>> sys.executable
'/Users/brianlynch/.local/share/virtualenvs/my_project-HsV6LrWY/bin/python'
```

#### Deactivate Enviornment

```
exit
```

#### Run command without activating the Enviornment

```bash
pipenv run python              # run python using the virtual enviornment
pipenv run python script.py    # run python script using the virtual enviornment
```

#### Install requirements.txt file

```bash
pipenv install -r requirements.txt
```

#### Create requirements.txt file

```
pipenv lock -r > requirements.txt
```

#### Install dev only package, e.g pytest

```bash
pipenv install pytest --dev
```

#### Uninstal package

```
pipenv uninstall requests
```

#### Recreate enviornment with different version of python

Modify python version in the Pipfile

```
pipenv --python 3.6
```

#### Remove virtual enviornment

Only remove enviornment, does not delete Pipfile

```
pipenv --rm
```

#### Create enviornment from Pipfile

```
pipenv install
```

#### Get path to virtual enviornment

```
pipenv --venv
```

#### Check for security vulnerabilities

```
pipenv check
```

#### View installed packages and dependencies

```
pipenv graph
```

#### Update Pipfile.lock

```
pipenv lock
```

#### Create enviornment using Pipfile.lock

```
pipenv install --ignore-pipfile
```

#### Enviornment Variables

```python
touch .env
echo 'SECRET_KEY="secret_key"'
pipenv run python
>>> import os
>>> os.environ['SECRET_KEY']
'MySecretKey'
```

