
from django.urls import path
from ppp import views

app_name='ppp'

urlpatterns=[

	path('',views.index,name='index'),


]
