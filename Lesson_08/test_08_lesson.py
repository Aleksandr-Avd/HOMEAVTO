import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = ""
id_negative="2132132132132132132"



@pytest.fixture(scope="module")
def сreate_project_id():
    payload = {
        "title": "new_project1",
        "users": {
             "48d0c348-a387-4230-adf2-fa4777fa02f0": "worker"
    }
}
    headers = {
        "Content-Type": "application/json",
        "Authorization":f"Bearer {TOKEN}"
        }

    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201
    return response.json()["id"]
    
@pytest.fixture(scope="session")
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
        }



def test_сreate_new_project_positive(headers):
    payload = {
        "title": "new project",
        "users": {
            "48d0c348-a387-4230-adf2-fa4777fa02f0": "worker"
    }
}
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201

# Пустое поле title
def test_сreate_new_project_negative(headers):
    payload = {
        "title": "",
        "users": {
             "48d0c348-a387-4230-adf2-fa4777fa02f0": "worker"
    }
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 400


def test_editing_project_positive(сreate_project_id,headers):
    
    payload = {
        "deleted": False,
        "title": "ГосУслуги",
        "users": {
            "48d0c348-a387-4230-adf2-fa4777fa02f0": "worker"
        }
    }
    
    response = requests.put(f"{BASE_URL}/{сreate_project_id}", json=payload, headers=headers)
    assert response.status_code == 200
   


# Некорректный id
def test_editing_project_negative(headers):
    payload = {
    "deleted": False,
    "title": "ГосУслуги",
    "users": {
        "48d0c348-a387-4230-adf2-fa4777fa02f0": "worker"
        }
    }
    
    response = requests.put(f"{BASE_URL}/{id_negative}", json=payload, headers=headers)
    assert response.status_code == 404



def test_get_by_id_positive(сreate_project_id,headers):
    response = requests.get(f"{BASE_URL}/{сreate_project_id}", headers=headers)
    assert response.status_code == 200


# Некорректный id
def test_get_by_id_negative(headers):
    response = requests.get(f"{BASE_URL}/{id_negative}", headers=headers)
    assert response.status_code == 404