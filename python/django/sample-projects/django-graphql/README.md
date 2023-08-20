#Integrating GraphQL API with Django Framework

## Tools Used
[Django 3](https://www.djangoproject.com/)  
[Graphene](https://graphene-python.org/): library for building GraphQL APIs in Python  
[Django GraphQL JWT](https://django-graphql-jwt.domake.io/en/latest/): JSON Web Token authentication for Django GraphQL  
[Relay](https://relay.dev/): production-ready GraphQL client for React  

[django-filter](https://django-filter.readthedocs.io/en/stable/guide/install.html): Generic, reusable application to alleviate writing some of the more mundane bits of view code  


## How to Add GraphQL to Django Project
install graphene  
`pip install graphene-django`

add to install apps in **settings.py**
``` python
INSTALLED_APPS = [
    ...
    "django.contrib.staticfiles", # Required for GraphiQL
    "graphene_django"
]
```

add URL for graphql
``` python
from django.conf.urls import url
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    url(r"graphql", GraphQLView.as_view(graphiql=True)),
]
```

create schema.py
```bash
touch movies/schema.py
```
```python
import graphene

class Query(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
```

add schema url to settings
```python
GRAPHENE = {
    'SCHEMA': 'movies.schema.schema'
}
```

add url
```python
from graphene_django.views import GraphQLView

urlpatterns = [
    ...
    path('graphql/', GraphQLView.as_view(graphiql=True))
]
```
