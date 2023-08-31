from django.urls import path
from . import views

app_name = 'url_shortener_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('api/shorten/', views.generate_short_key, name='shorten_url'),  # Define the API URL pattern here
    path('<str:short_key>/', views.redirect_original, name='redirect_original'),
]