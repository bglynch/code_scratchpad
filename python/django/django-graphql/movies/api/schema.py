import graphene
from graphene_django.types import DjangoObjectType

from .models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        return "Old Movie" if self.year < 2000 else "New Movie"


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_movie(self, info, **kwargs):
        movie_id = kwargs.get('id')
        title = kwargs.get('title')

        if movie_id is not None:
            return Movie.objects.get(pk=movie_id)
        if title is not None:
            return Movie.objects.get(title=title)

        return None
