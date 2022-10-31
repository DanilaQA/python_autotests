import importlib

import pytest
import requests

response_pet = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 88005553535,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "QAshka",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})