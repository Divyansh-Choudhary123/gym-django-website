from django.urls import path
from.import views

urlpatterns = [
   path('',views.index,name='index'),
   path('care',views.care,name='care'),
   path('mind',views.mind,name='mind'),
   path('store',views.store,name='store'),
   path('loginData',views.loginData,name='loginData')
]