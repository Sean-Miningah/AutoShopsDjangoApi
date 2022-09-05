from django.urls import path 
from graphene_django.views import GraphQLView 
from technician.schema import schema 

urlpatterns = [
    path("technician", GraphQLView.as_view(graphiql=True, schema=schema)),
]