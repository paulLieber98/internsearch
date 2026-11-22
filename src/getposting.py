import requests

request = requests.get("https://himalayas.app/jobs/api") #not using the "/search" api because this one w/o is unfiltered.

print(request)