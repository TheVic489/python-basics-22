import pprint as pp
import requests
from requests.models import Response

 # Make a GET Request
url: str = 'https://animechan.vercel.app/api/random'

response: Response = requests.get(url)

# Print Response
print(response)

# Print json content
pp.pprint(response.json())