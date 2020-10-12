from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('parts/', views.parts_index, name='index'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:part_id>/', views.parts_detail, name='detail'),
]
