from django.urls import path

from . import views
urlpatterns = [
    #   path(...) : Django define a URL
    #   "<month>" dynamic URL parameter, Django sẽ bắt giá trị nằm ở vị trí này trong URL và truyền nó vào hàm view
    #   views.monthly_challenge : Là hàm view sẽ xử lý request khi URL khớp với pattern trên
    #
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("", views.index)
]