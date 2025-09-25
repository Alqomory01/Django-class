from django.urls import path
from . import views

urlpatterns =[
    path('', views.event_form),
    path('event/<int:event_id>', views.event_details , name='event_details')
]