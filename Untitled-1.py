
import json
from urllib.request import urlopen
from urllib.parse import urlencode
params = dict(q="Sausages", format="json")
handle = urlopen('http://api.duckduckgo.com' + "?" + urlencode(params))
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)

results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])

# do a search with requests
import requests
params = dict(q='Sausages', format='json')
parsed = requests.get('http://api.duckduckgo.com/', params=params).json()

results = parsed['RelatedTopics']
for r in results:
    if "Text" in r:
        print(r["FirstURL"] + ' - ' + r['Text'])

# both codes do the same thing, but the second is simpler to read and understand

# do a search with duckduckgo module
import duckduckgo
for r in duckduckgo.query('Sausages').results:
    print(r.url + ' - ' + r.text)