# Start Django App

---



```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Django
django-admin startproject $1 .
# create .gitignore
echo db.sqlite3 > .gitignore
# update ALLOWED_HOSTS  sed -i "/ALLOWED_HOSTS/s/\[\]/\['$C9_HOSTNAME'\]/g" ./$1/settings.py 
# migrate to create database
python3 manage.py migrate
# create superuser
python3 manage.py createsuperuser  # update to create default
# Create folders and blank files for custom static files
mkdir -p static/css
wget https://raw.githubusercontent.com/bglynch/templates/master/css/bootstrap.css -O ./static/css/style.css 
mkdir -p static/js
touch static/js/custom.js
mkdir -p static/lib
mkdir -p static/images
# add static files locations to settings
echo STATICFILES_DIRS = \(os.path.join\(BASE_DIR, 'static'\), \) >> ./$DJANGO_PROJECT/settings.py 
echo STATIC_ROOT = os.path.join\(BASE_DIR, 'static'\) >> ./$DJANGO_PROJECT/settings.py 

# # create template file and add basic base.html
mkdir -p templates
wget https://raw.githubusercontent.com/bglynch/templates/master/django/html/bootstrap-home.html -O ./templates/base.html 

# add templates to settings.py
sed -i "/DIRS/s/\[\]/\[os.path.join\(BASE_DIR, 'templates'\)\]/g" ./$DJANGO_PROJECT/settings.py
# Install pillow
sudo pip3 install pillow
# add media folder
mkdir -p media
# add media context processors to settings.py
sed -i -e "/'django.contrib.messages.context_processors.messages',/a\                'django.template.context_processors.media'," ./$DJANGO_PROJECT/settings.py
# add media roots to settings.py
echo " "
echo MEDIA_URL = '/media/' >> ./$DJANGO_PROJECT/settings.py 
echo MEDIA_ROOT = os.path.join\(BASE_DIR, 'media'\) >> ./$DJANGO_PROJECT/settings.py 
pip3 freeze --local > requirements.txt
```

