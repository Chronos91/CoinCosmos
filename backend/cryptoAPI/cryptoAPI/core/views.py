import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_crypto_data(request):
	url = "https://api.coinranking.com/v2/coins"

	querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}

	headers = {
		"x-rapidapi-key": "coinranking8ba95e1df21b97ad930c0dcd7689be1016c2afd62210b5ddcoinranking8ba95e1df21b97ad930c0dcd7689be1016c2afd62210b5dd",
		"x-rapidapi-host": "coinranking1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	return Response(response.json())


@api_view(['GET'])
def get_news_data(request):
	url = "https://cryptocurrency-news2.p.rapidapi.com/v1/cryptodaily"

	headers = {
		"x-rapidapi-key": "fed4832865mshe1cbd70d271a228p18f4a9jsnbbb8600f514a",
		"x-rapidapi-host": "cryptocurrency-news2.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)
	
	return Response(response.json())
