"""
URL configuration for mypage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from challenges import views as challenges_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add this line to handle the root URL ("")
    path(
        "", challenges_views.index, name="home-index"
    ),  # Point root URL to challenges' index view
    path(
        "challenges/", include("challenges.urls")
    ),  # overall Django app should handle request sent to challenges,
    # then, urls in challenges app will be used if it is reached
]
