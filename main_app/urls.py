from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('',  views.parts_index, name='index'),
    path('parts/', views.parts_index, name='index'),
    path('parts/<int:part_id>/', views.parts_detail, name='parts_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:part_id>/', views.parts_detail, name='detail'),
    path('parts/<int:part_id>/update/',
         views.PartUpdate.as_view(), name='parts_update'),
    path('parts/<int:pk>/delete/',
         views.PartDelete.as_view(), name="parts_delete")
]
