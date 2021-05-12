## Data Science Project Template

Code from the blog found here:

https://www.bglynch.com/blog/data-science-setup.html

![](https://www.bglynch.com/images/pexels-karolina-grabowska-4207707.jpg)



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
pip freeze > requirements.txt
mkdir data
mkdir data/raw
mkdir src
mkdir src/tests
mkdir notebooks
touch data/raw.RawData.md
touch src/custom_functions.py
touch src/tests/test_custom_functions.py
touch .env
echo .env >> .gitignore
```

