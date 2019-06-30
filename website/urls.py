from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^index', views.index, name="index"),
    re_path(r'^signup', views.signup, name='signup'),
    re_path(r'^login', auth_views.LoginView.as_view(template_name = 'website/login.html'), name='login'),
    re_path(r'^logout', auth_views.LogoutView.as_view(next_page = '/'),  name='logout'),
    re_path(r'^account', views.account, name="account"),
    re_path(r'^result', views.result, name="result"),
    re_path(r'^product/(?P<product_id>.+)', views.product, name="product"),
    re_path(r'^favorites', views.favorites, name="favorites"),
    re_path(r'^save/(?P<product_id>.+)', views.save, name="save"),
    re_path(r'^remove/(?P<product_id>.+)', views.remove, name="remove"),
    re_path(r'^contact', views.contact, name="contact"),
    re_path(r'^legal_terms', views.legal_terms, name="legal_terms"),
]