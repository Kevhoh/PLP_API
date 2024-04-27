import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["type"]

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]
  # Example 3
  # reponse3 = requests.get('https://api.thedogapi.com/v1/images/')
  # data3 = reponse3.json()
  # result3 = data3[0]["url"]



  return render(request, 'templates/index.html', {'result': result, 'result2': result2})