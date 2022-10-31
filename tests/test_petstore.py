import importlib

import pytest
import requests

petId = 88005553535
URL = 'https://petstore.swagger.io/v2'
response_pet = requests.get(f'{URL}/pet/{petId}')


def test_statuscode():
    assert response_pet.status_code == 200

def test_response_name():
    assert response_pet.json()['name'] == 'QAshka'