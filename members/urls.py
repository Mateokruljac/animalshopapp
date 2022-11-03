from django.urls import path

from . import views

urlpatterns = [
    path("login",views.user_login,name = "customer_login"),
    path("regiser",views.user_register,name = "customer_register"),
    path("logout",views.user_logout, name = "customer_logout"),
    path("customer",views.customer_page,name = "customer"),
    
    #customer action
    path("update-item",views.update_item,name = "update-item"),
    path("proccess-order",views.proccess_order,name = "procces-order")
]
