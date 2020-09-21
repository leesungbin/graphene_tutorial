from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from graphql_playground.views import GraphQLPlaygroundView

from schema import schema
# print(schema)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('playground/',
         GraphQLPlaygroundView.as_view(endpoint="https://test-mzwbacd5xa-an.a.run.app/graphql/")),
]
