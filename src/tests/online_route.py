import requests


def test_index():
   response = requests.get('http://localhost:5001/')
   assert response.status_code == 200
   assert 'Hello, World!' in response.text

