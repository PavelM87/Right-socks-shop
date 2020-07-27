from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<slug:item_slug>/', views.item, name='item'),
    path('contacts', views.contacts, name='contacts'),
]