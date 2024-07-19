from django.urls import path
from account.views import Home

urlpatterns = [
    path("home/", Home.as_view(), name="home"),
]
