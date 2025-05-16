from django.urls import path
from . import views

urlpatterns = [
    path('', views.salom),
    path('<str:sinf>/<str:name>', views.info)
]