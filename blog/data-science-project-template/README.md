## Data Science Project Template

Code from the blog found here:

https://www.bglynch.com/blog/data-science-setup.html



All commands

```bash
mkdir project
cd project
virtualenv -p python3 venv
source venv/bin/activate
pip install pandas
pip install numpy
pip install jupyterlab
pip install python-decouple
mkdir data
mkdir data/raw
mkdir src
mkdir src/tests
touch data/raw.RawData.md
touch src/custom_functions.py
touch src/tests/test_custom_functions.py
touch .env
echo .env >> .gitignore
pip freeze > requirements.txt
```

