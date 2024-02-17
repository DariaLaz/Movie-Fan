import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from decouple import config
from dotenv import load_dotenv


class MovieSarpView(APIView):
    def get(self, request):
        load_dotenv()
        SERP_API_KEY = config(
            'SERP_API_KEY', default='default_value_if_not_present')

        query = request.GET.get('q')
        if not query:
            return Response({'movies': []}, status=status.HTTP_200_OK)

        url = f'https://serpapi.com/search.json?engine=google_play_movies&q={query}'

        params = {
            "engine": "google_play_movies",
            "q": f"{query}",
            "api_key": f'{SERP_API_KEY}',
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()
            data = data.get('organic_results')[0].get('items')
            return Response({'movies': data}, status=status.HTTP_200_OK)
        except:
            return Response({'movies': []}, status=status.HTTP_200_OK)
