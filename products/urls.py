from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('simple-list/', views.product_list_simple, name='product_list_simple'),
    path('list-view/', views.ProductListView.as_view(), name='product_list'),
    path('contact-register/', views.contact_view, name='contact_register'),
    path('product-create/', views.products_create_view, name='product_create'),
]
