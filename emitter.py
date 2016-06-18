import requests
from datetime import datetime
import os

now = datetime.now()
url = os.environ['SERVER_URL'] + '/docker-test'
response = requests.post(url, data = {'foo': 'bar'})

print(
    "\nTotal Time: ",
    (datetime.now() - now).total_seconds()
)
