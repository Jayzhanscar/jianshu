import requests
import json
url = 'http://api.yytianqi.com/forecast7d?city=CH210101&key=1ekloh84uj6m2nlm'
reponse = requests.get(str(url))
print(reponse.text)


def tianqi():
    # tianqi api  task  callback a json data
    url = 'http://api.yytianqi.com/forecast7d?city=CH210101&key=1ekloh84uj6m2nlm'
    reponse = requests.get(str(url))
    return json.loads(reponse.text)
