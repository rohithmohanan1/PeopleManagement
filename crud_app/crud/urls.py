from django.urls import path
from .views import *

urlpatterns = [
    path('', list),
    path('list/', add),
    path('<id>', detail),
    path('<id>/update', update),
    path('<id>/delete', delete),
]