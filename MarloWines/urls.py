"""
URL configuration for MarloWines project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Wines.views import *

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('homepage/' , Landing_page, name='homepage'),
    path('products/' , Products_page, name='productspage'),    
    path('login/' , Login, name='loginpage'),    
    path('register/' , Register, name='registerpage'),   
    path('logout/' , Logout, name='logout'), 
    path('product_processing/', Product_Processing, name='product_processing'),
    path('product1/', Product_1, name='product_1'),
    path('product2/', Product_2, name='product_2'),
    path('product3/', Product_3, name='product_3'),
    path('product4/', Product_4, name='product_4'),
    path('product5/', Product_5, name='product_5'),
    path('product6/', Product_6, name='product_6'),
    path('ContactUs/', Contact_Us, name='ContactUs'),
    path('cart/', crate, name='cartpage')
    
]
