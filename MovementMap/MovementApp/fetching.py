import requests

def fetch_all():
  url = 'http://www.nomisweb.co.uk/api/v01/dataset/NM_162_1.jsonstat.json?date=latest&Gender=0,1,2&Age=11,12'
  return requests.get(url).json()
