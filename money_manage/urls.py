from django.urls import path

from money_manage.views import home

urlpatterns = [
    path('', home),
]
