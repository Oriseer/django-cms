from django.urls import path
from .views import *

app_name = 'client'

urlpatterns = [
    path('client/', ClientListView.as_view(), name="client-list"),
    path('view/<int:pk>', ClientDetailView.as_view(), name="client-detail"),
    path('update/<int:pk>', ClientUpdateView.as_view(), name="client-update"),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name="client-delete"),
    path('create/', client_create, name="client-create")
]