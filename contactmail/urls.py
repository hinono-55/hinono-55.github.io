from django.urls import path
from . import views

app_name='contactmail'

urlpatterns=[
    path('contact/', views.ContactmailView.as_view(), name='contact'),
]