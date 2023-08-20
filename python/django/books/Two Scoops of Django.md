# Two Scoops of Django

---

## Project Layout

```bash
<repository_root>/
   ├── <configuration_root>/
   ├── <django_project_root>/
```

#### Two Tier Approach:

#### Top Level: <repository_root>

> absolute root directory of the project

#### Second Level: `<django_project_root>`

> root of the actual Django project.

#### Second Level: `<configuration_root>`

> settings module and base URLConf (urls.py)

#### Sample Layout

```python
icecreamratings_project
├── config/
│   ├── settings/
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── docs/
├── icecreamratings/
│   ├── media/          # Development only!
│   ├── products/       # App for managing and displaying ice cream brands.
│   ├── profiles/       # App for managing and displaying user pro- files.
│   ├── ratings/        # App for managing user ratings.
│   ├── static/         
│   └── templates/      # Where you put your site-wide Django tem- plates.
├── .gitignore
├── Makefile
├── README.md
├── manage.py
└── requirements.txt
```



### Apps

- As a general rule, the **app’s name should be a plural version** of the app’s main model,

- Try and keep your apps small. Remember, it’s better to have many small apps than to have a few giant apps.

- ```python
  # COMMON APP MODULES  |  # UNCOMMON APP MODULES
  scoops/               |  scoops/                              
  ├── __init__.py       |  ├── api/                    # isolating the various modules needed when creating an api.
  ├── admin.py          |  ├── behaviors.py            # locating model mixins
  ├── apps.py           |  ├── constants.py            
  ├── forms.py          |  ├── context_processors.py   
  ├── management/       |  ├── decorators.py           
  ├── migrations/       |  ├── db/                     
  ├── models.py         |  ├── exceptions.py           
  ├── templatetags/     |  ├── fields.py               
  ├── tests/            |  ├── factories.py            # test data factories.
  ├── urls.py           |  ├── helpers.py              
  ├── views.py          |  ├── managers.py             
                        |  ├── middleware.py           
                        |  ├── schema.py               
                        |  ├── signals.py              
                        |  ├── utils.py                
                        |  ├── viewmixins.py           
  ```

  

---



## Settings

- Instead of having one settings.py file, with this setup you have a settings/ directory containing your settings files

  ```python
  # Example
  settings/
  ├── __init__.py    # 
  ├── base.py        # Settings common to all instances of the project
  ├── local.py       # Local development-specific settings include DEBUG mode, log level, and activation of developer tools like django-debug-toolbar.
  ├── staging.py     # running a semi-private version of the site on a production server.
  ├── test.py        # running tests including test runners, in-memory database definitions, and log settings.
  ├── production.py  # This file con- tains production-level settings only
  ```

  **Note**: Each settings module should have its own corresponding requirements file

#### Running App With Different Settings 

##### Command Line

> ```bash
> python manage.py shell --settings=config.settings.local
> python manage.py runserver --settings=config.settings.local
> ```
##### Settings FIle

> ```python
> # config/settings/local.py
> DJANGO_SETTINGS_MODULE = 'twoscoops.settings.local'
> ```

##### Sample local settings

> ```python
> from .base import *
> 
> DEBUG = True
> 
> EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
> 
> DATABASES = {
>   'default': {
>       'ENGINE': 'django.db.backends.postgresql',
>       'NAME': 'twoscoops',
>       'HOST': 'localhost',
>   } 
> }
> 
> INSTALLED_APPS += ['debug_toolbar', ]
> ```

### Multiple Requirements Files

- good practice for each settings file to have its own corresponding requirements file.
- eate a requirements/ di- rectory in the <repository_root>. Then create ‘.txt’ files that match the contents of your settings directory

> ```bash
> requirements/
>    ├── base.txt
>    ├── local.txt
>    ├── staging.txt
>    ├── production.txt
> ```

- Should inherit from base.txt

> ```bash
> # requirements/base.txt
> Django==3.2.0
> psycopg2-binary==2.8.8
> djangorestframework==3.11.0
> ```
>
> ```bash
> # requirements/local.txt
> -r base.txt # includes the base.txt requirements file
> coverage==5.1
> django-debug-toolbar==2.2
> ```
>
> ```bash
> # Installation
> pip install -r requirements/local.txt
> ```

#### Handling File Paths in Settings

-  **<u>NEVER</u>** hardcode file paths in Django settings files

##### Bad Example

> ```python
> # settings/base.py
> # Configuring MEDIA_ROOT
> # DON’T DO THIS! Hardcoded to just one user's preferences
> MEDIA_ROOT = '/Users/pydanny/twoscoops_project/media'
> 
> # Configuring STATIC_ROOT
> # DON’T DO THIS! Hardcoded to just one user's preferences
> STATIC_ROOT = '/Users/pydanny/twoscoops_project/collected_static'
> 
> # Configuring STATICFILES_DIRS
> # DON’T DO THIS! Hardcoded to just one user's preferences
> STATICFILES_DIRS = ['/Users/pydanny/twoscoops_project/static']
> 
> # Configuring TEMPLATES
> # DON’T DO THIS! Hardcoded to just one user's preferences
> TEMPLATES = [
>   {
>     'BACKEND':
>       'django.template.backends.django.DjangoTemplates',
>     DIRS: ['/Users/pydanny/twoscoops_project/templates',]
>   },
> ]
> 
> ```

##### Good Example

> Option 1: Using Path
>
> ```python
> # At the top of settings/base.py
> from pathlib import Path
> 
> BASE_DIR = Path(__file__).resolve().parent.parent.parent
> 
> MEDIA_ROOT = BASE_DIR / 'media'
> STATIC_ROOT = BASE_DIR / 'static_root'
> STATICFILES_DIRS = [BASE_DIR / 'static']
> TEMPLATES = [
>   {
>     'BACKEND':
>       'django.template.backends.django.DjangoTemplates',
>     DIRS: [BASE_DIR / 'templates']
>   },
> ]
> ```
>
> Option 2: Using os
>
> ```python
>  # At the top of settings/base.py
> from os.path import abspath, dirname, join
> 
> def root(*dirs):
>   base_dir = join(dirname(__file__), '..', '..') 
>     return abspath(join(base_dir, *dirs))
> 
> BASE_DIR = root()
> MEDIA_ROOT = root('media')
> STATIC_ROOT = root('static_root')
> STATICFILES_DIRS = [root('static')]
> 
> TEMPLATES = [
>     {
>        'BACKEND':
>        'django.template.backends.django.DjangoTemplates',
>        DIRS: [root('templates')]
>     },
> ]
> ```



---



## Models

#### Make Choices and Sub-Choices Model Constants

>```python
> # orders/models.py
>from django.db import models
>
>class IceCreamOrder(models.Model): 
>    FLAVOR_CHOCOLATE = 'ch' 
>    FLAVOR_VANILLA = 'vn' 
>    FLAVOR_STRAWBERRY = 'st' 
>    FLAVOR_CHUNKY_MUNKY = 'cm'
>    FLAVOR_CHOICES = (
>        (FLAVOR_CHOCOLATE, 'Chocolate'),
>        (FLAVOR_VANILLA, 'Vanilla'),
>        (FLAVOR_STRAWBERRY, 'Strawberry'),
>        (FLAVOR_CHUNKY_MUNKY, 'Chunky Munky')
>    )
>  
>    flavor = models.CharField(max_length=2,choices=FLAVOR_CHOICES)
>    ```
>  
>```python
># access the choice
>from orders.models import IceCreamOrder
>IceCreamOrder.objects.filter(flavor=IceCreamOrder.FLAVOR_CHOCOLATE) 
>>>> [<icecreamorder: 35>, <icecreamorder: 42>, <icecreamorder: 49>]
>```

##### Using Enumeration Types for Choices

> ```python
> from django.db import models
> 
> class IceCreamOrder(models.Model): 
>     class Flavors(models.TextChoices):
>        CHOCOLATE = 'ch', 'Chocolate'
>        VANILLA = 'vn', 'Vanilla'
>        STRAWBERRY = 'st', 'Strawberry'
>        CHUNKY_MUNKY = 'cm', 'Chunky Munky'
>     
>       flavor = models.CharField(
>          max_length=2,
>          choices=Flavors.choices
>       )
> 
>       # Usage
>     from orders.models import IceCreamOrder
>     IceCreamOrder.objects.filter(flavor=IceCreamOrder.Flavors.CHOCOLATE) 
>     >>> [<icecreamorder: 35>, <icecreamorder: 42>, <icecreamorder: 49>]
> ```

## 

---



## Function Based View

#### Guidelines

- Less view code is better.
- Never repeat code in views.
- Views should handle presentation logic. 
  Try to keep business logic in models when possible, or in forms if you must.
- Keep your views simple.
- Use them to write custom 403, 404, and 500 error handlers.
- Complex nested-if blocks are to be avoided.

##### Best Pratices

> ```python
> # 🔴🔴🔴🔴🔴🔴🔴🔴 ORIGIONAL
> from django.core.exceptions import PermissionDenied 
> from django.http import HttpRequest
> 
> def check_sprinkle_rights(request: HttpRequest) -> HttpRequest: 
>     if request.user.can_sprinkle or request.user.is_staff:
>     return request
> 	
>     # Return a HTTP 403 back to the user
>   raise PermissionDenied
> ```
>
> Instead of returning the origional request, we now add the field `request.can_sprinkle = True` and check for that in the template
>
> ```python
> # 🟢🟢🟢🟢🟢🟢🟢🟢 OPTIMISED
> from django.core.exceptions import PermissionDenied 
> from django.http import HttpRequest
> 
> def check_sprinkles(request: HttpRequest) -> HttpRequest: 
>     if request.user.can_sprinkle or request.user.is_staff:
>        # By adding this value here it means our display templates
>        #   can be more generic. We don't need to have
> 
>        request.can_sprinkle = True 
>        return request
>     # Return a HTTP 403 back to the user
>   raise PermissionDenied
> 
> # --------------------------------------------------- template code
> {% if request.can_sprinkle %} 
> ```
>
> .
>
> ```python
> # sprinkles/views.py
> from django.shortcuts import get_object_or_404 
> from django.shortcuts import render
> from django.http import HttpRequest, HttpResponse
> from .models import Sprinkle
> from .utils import check_sprinkles
> 
> def sprinkle_list(request: HttpRequest) -> HttpResponse: 
>     """Standard list view"""
>     request = check_sprinkles(request)
>   return render(request, "sprinkles/sprinkle_list.html", {"sprinkles": Sprinkle.objects.all()})
> 
> def sprinkle_detail(request: HttpRequest, pk: int) -> HttpResponse: 
>     """Standard detail view"""
>     request = check_sprinkles(request)
>     sprinkle = get_object_or_404(Sprinkle, pk=pk)
>   return render(request, "sprinkles/sprinkle_detail.html", {"sprinkle": sprinkle})
> 
> def sprinkle_preview(request: HttpRequest) -> HttpResponse: 
>     """Preview of new sprinkle, but without the check_sprinkles function being used."""
>   sprinkle = Sprinkle.objects.all() 
>     return render(request,"sprinkles/sprinkle_preview.html",{"sprinkle": sprinkle})
> ```



---



### Decorators

Sample Decorator Template

> ```python
> import functools
> 
> def decorator(view_func): 
>     @functools.wraps(view_func)
>   def new_view_func(request, *args, **kwargs):
>       # You can modify the request (HttpRequest) object here.
>     response = view_func(request, *args, **kwargs)
>     # You can modify the response (HttpResponse) object here. 
>       return response
>   return new_view_func
> ```

Sample Using Code Above

> Create decorator to check sprinkles
>
> ```python
> # sprinkles/decorators.py
> import functools 
> from . import utils
> 
> # based off the decorator template from the previous example
> def check_sprinkles(view_func):
> 	"""Check if a user can add sprinkles""" 
>   	@functools.wraps(view_func)
> 	def new_view_func(request, *args, **kwargs):
>   		request = utils.can_sprinkle(request) # Act on the request object with  utils.can_sprinkle()
>       response = view_func(request, *args, **kwargs)  # Call the view function
> 		return response                                 # Return the HttpResponse object
> 
>   return new_view_func
> ```
>
> Use the decorator
>
> ```python
> # sprinkles/views.py
> from django.shortcuts import get_object_or_404, render 
> from .decorators import check_sprinkles
> from .models import Sprinkle
> 
> # Attach the decorator to the view
> @check_sprinkles
> def sprinkle_detail(request: HttpRequest, pk: int) -> HttpResponse: 
>   """Standard detail view"""
> 	sprinkle = get_object_or_404(Sprinkle, pk=pk)
> 	return render(request, "sprinkles/sprinkle_detail.html", {"sprinkle": sprinkle})
> ```



---



## Class-Based Views

> a Django view is just a callable that **accepts a request** object and **returns a response.**
>
> - For function-based views (FBVs), the view function is that callable
> - For CBVs, the view class provides an as_view() class method that returns the callable
>
> https://ccbv.co.uk/: Detailed descriptions, with full methods and attributes, for each of [Django](https://djangoproject.com/)'s class-based generic views