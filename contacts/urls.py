from django.urls import path
from . import views #viewsにあるすべてを持ってくる

#  listings

urlpatterns = [
    path('contact', views.contact, name='contact'),
]

