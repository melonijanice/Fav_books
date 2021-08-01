from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books',views.book),
    path('add_book',views.add_book),
    path('books/<int:id>',views.view_books),
    path('add_to_fav/<int:id>/<int:_from>',views.add_to_fav),
    path('update_delete/<int:id>',views.update_delete),
    path('remove_from_fav/<int:id>',views.remove_from_fav),
    path('view_fav',views.view_fav)
]