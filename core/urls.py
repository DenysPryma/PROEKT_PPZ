from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('favorites/', views.favorites, name='favorites'),
    path('product/', views.product_list, name='product'),
    path('cart/', views.cart, name='cart'),
    path('save_cart/<int:product_id>/', views.save_cart, name='save_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('order/<int:order_id>/', views.create_ticket_pay, name='create_ticket_pay'),
]