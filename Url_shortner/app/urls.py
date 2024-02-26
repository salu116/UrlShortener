from django.urls import path, include
from .views import UrlShortner

urlpatterns = [
   path('shorturl/', UrlShortner.as_view(), name="url_shortner")
]
