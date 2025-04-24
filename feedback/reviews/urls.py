from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review, name='review'),
    path('thank-you/', views.thank_you, name='thank_you'),
    # API endpoints
    path('api/reviews/', views.review_list, name='review-list'),
    path('api/reviews/<int:pk>/', views.review_detail, name='review-detail'),
] 