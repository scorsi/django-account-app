from django.conf.urls import url
from .views import register, logout, login, edit, edit_password, validation

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
    url(r'^edit/password/', edit_password, name='password'),
    url(r'^edit/', edit, name='edit'),
    url(r'^validation/', validation, name='validation'),
]
