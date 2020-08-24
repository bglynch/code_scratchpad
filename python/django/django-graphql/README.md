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
