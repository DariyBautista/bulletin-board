from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('create/', views.AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
]
