from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name="main_page"),
    path('category/<int:category_id>/',
         category_page,
         name="category_page"),

    path('article/<int:article_id>/', receipt_detail,
         name="receipt_detail")
]