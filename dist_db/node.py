import requests
from thing import Thing

def get_thing(url, id):
    res = requests.get('{0}/things/{1}'.format(url, id))
    res.raise_for_status()
    return Thing.from_json(res.json())

def put_thing(url, thing):
    res = requests.post(
              '{0}/things'.format(url),
              data=str(thing),
              headers={'Content-Type': 'application/json'})
    res.raise_for_status()
    return Thing.from_json(res.json())

