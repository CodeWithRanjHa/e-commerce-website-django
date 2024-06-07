from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.view_cart, name='carts'),
    path('remove-cart/<int:pk>', views.remove_cart, name='remove-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('plus_cart', views.plus_cart, name='plus_cart'),  
    path('minus_cart/', views.minus_cart, name='minus_cart'),
    path('order_placed/', views.order_placed, name='order_placed'),
    path('orders/', views.orders, name='orders'),
    path('search/', views.search_bar, name='search'),
    path('get_cart_count/', views.get_cart_count, name='get_cart_count'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('buynow/', views.buy_now, name='buy_now'),


]
