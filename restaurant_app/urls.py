from django.urls import path
from . import views 

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register_user, name='register_user'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('menu_item/',views.menu_item,name='menu_item'),
    path('order/',views.order,name='order'),
    path('table/',views.table,name='table'),
    path('menu_categories/',views.menu_categories,name='menu_categories'),
    path('orderitem',views.order_item,name='orderitem'),
    path('bill/',views.bill,name='bill'),
    path('home', views.home, name='home'), 
   
] 