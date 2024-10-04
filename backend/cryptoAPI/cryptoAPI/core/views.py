import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_crypto_data(request):
	url = "https://coinranking1.p.rapidapi.com/stats"

	querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}

	headers = {
		"x-rapidapi-key": "fed4832865mshe1cbd70d271a228p18f4a9jsnbbb8600f514a",
		"x-rapidapi-host": "coinranking1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	return Response(response.json())
