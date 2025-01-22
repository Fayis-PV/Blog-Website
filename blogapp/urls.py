from django.urls import path
from . import views

# Create all urls here

urlpatterns = [
    path("",views.home,name='home'),
    # path(),
]
