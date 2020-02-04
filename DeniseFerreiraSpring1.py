import requests
import json

url='https://jobs.github.com/positions?description=python&location=new+york'
  result = []
  for i in range(0,226+1):
    response = requests.get(url, params= {'list':i, 'per_list' :50})
    if response.status_code ==226:
        result += response.json()
    data = response.json()





