from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-pickup', views.book, name='book'),
    path('user.html',views.user,name="user"),
]
