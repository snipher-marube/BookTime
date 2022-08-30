from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('contact/', views.ContactUSView.as_view(), name='contact'),
    path('products/<slug:tag>/', views.ProductListView.as_view(), name='products'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'),
]
