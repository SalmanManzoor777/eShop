
from django.contrib import admin
from django.urls import path,re_path
from .views import *

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/', category, name='category'),
    path("home/", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="products"),
#    path('products/<slug>/', ProductView.as_view(), name='products'),
    path('product/', product, name='product'),
    path("addtocart/<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    # path("addtocart/", AddToCartView.as_view(), name="addtocart"),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('account/', account, name='account'),
    


]
