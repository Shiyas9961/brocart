from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_page, name = 'account'),
    path('logout', views.signout, name = 'logout')
]
