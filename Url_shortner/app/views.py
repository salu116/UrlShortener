from django.shortcuts import render
import pyshorteners
from rest_framework.views import APIView
from rest_framework.response import Response

class UrlShortner(APIView):
   def post(self, request):
        url = request.data.get('url')
        shortener = pyshorteners.Shortener()
        try:
            short_url = shortener.tinyurl.short(url)
            return Response({'short_url': short_url})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
