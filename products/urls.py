from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('feedback-report/', views.feedback_report, name='feedback_report'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]