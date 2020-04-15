from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /turnips/20200414/best_price/
    path('<int:date>/best_price', views.best_price, name='best_price'),
    # ex: /turnips/20200414/input/
    path('<int:date>/input', views.input_price, name='input_price'),
]