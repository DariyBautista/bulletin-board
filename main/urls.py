# urls.py (основний або в окремому додатку, наприклад `main`)
from django.urls import path
from .views import HomePageView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
