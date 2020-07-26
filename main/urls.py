from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts'),
    path('classic', views.classic, name='item-classic'),
    path('funeral', views.funeral, name='item-funeral'),
    path('cat-face', views.cat_face, name='item-cat'),
    path('pink', views.pink, name='pink'),
]