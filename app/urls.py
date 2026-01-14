from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create_view, name='product_create'),
    path('products/<int:product_id>/', views.product_datail, name='product_detail'),  # поправь опечатку datail → detail
]
