from django.urls import path
from .views import *
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('shop', ItemView.as_view(), name = 'shop'),
    path('product/<slug>', SingleView.as_view(), name = 'product'),
    path('search', SearchView.as_view(), name = 'search'),
    path('about', AboutView.as_view(), name = 'about'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('cart', cart, name='cart'),
    path('ad_to_cart', add_to_cart, name='add_to_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('contact', ContactView.as_view(), name='contact'),
    path('contactus', contactus, name = 'contactus'),
    path('order', order, name = 'order'),
    path('checkout', checkout, name = 'checkout'),

]