from django.urls import path

from . import views
urlpatterns = [
    path("january", views.index), #if a request reaches "jamuary" => exe index funtion of view
    path("february", views.index)
]