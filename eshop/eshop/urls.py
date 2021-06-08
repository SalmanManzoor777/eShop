"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    ProductView,
    HomeView,
    OrderSummaryView,
    index,
    category,
    cart,
    checkout,
    account,
    product

)

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/', category, name='category'),
    path('home/', HomeView.as_view(), name='home'),
    path('products/<slug>/', ProductView.as_view(), name='products'),
    path('product/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('account/', account, name='account'),
    


]
