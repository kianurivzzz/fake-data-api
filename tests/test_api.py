import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_read_root():
    response = client.get('/', follow_redirects=False)
    assert response.status_code == 307


def test_get_profile():
    response = client.get('/profile')
    assert response.status_code == 200
    data = response.json()
    assert 'profile' in data
    assert 'timestamp' in data
    assert 'datetime' in data


def test_get_profile_with_count():
    response = client.get('/profile?count=5')
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'count' in data
    assert data['count'] == 5
    assert len(data['data']) == 5


def test_get_profile_with_locale():
    response = client.get('/profile?locale=ru_RU')
    assert response.status_code == 200
    data = response.json()
    assert 'profile' in data


def test_get_name():
    response = client.get('/name')
    assert response.status_code == 200
    data = response.json()
    assert 'full_name' in data
    assert 'first_name' in data
    assert 'last_name' in data
    assert 'timestamp' in data


def test_get_name_with_count():
    response = client.get('/name?count=3')
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert data['count'] == 3


def test_get_address():
    response = client.get('/address')
    assert response.status_code == 200
    data = response.json()
    assert 'address' in data


def test_get_address_detailed():
    response = client.get('/address?detailed=true')
    assert response.status_code == 200
    data = response.json()
    assert 'address' in data
    assert 'city' in data
    assert 'country' in data
    assert 'zipcode' in data


def test_get_email():
    response = client.get('/email')
    assert response.status_code == 200
    data = response.json()
    assert 'email' in data
    assert '@' in data['email']


def test_get_job():
    response = client.get('/job')
    assert response.status_code == 200
    data = response.json()
    assert 'job' in data


def test_get_text():
    response = client.get('/text')
    assert response.status_code == 200
    data = response.json()
    assert 'text' in data


def test_get_text_with_max_chars():
    response = client.get('/text?max_chars=50')
    assert response.status_code == 200
    data = response.json()
    assert 'text' in data
    assert len(data['text']) <= 50


def test_get_ip():
    response = client.get('/ip')
    assert response.status_code == 200
    data = response.json()
    assert 'ipv4_address' in data


def test_get_ipv6():
    response = client.get('/ip?ipv6=true')
    assert response.status_code == 200
    data = response.json()
    assert 'ipv6_address' in data
    assert ':' in data['ipv6_address']


def test_get_mac():
    response = client.get('/mac')
    assert response.status_code == 200
    data = response.json()
    assert 'mac_address' in data


def test_get_phone():
    response = client.get('/phone')
    assert response.status_code == 200
    data = response.json()
    assert 'phone_number' in data


def test_get_company():
    response = client.get('/company')
    assert response.status_code == 200
    data = response.json()
    assert 'company' in data


def test_get_url():
    response = client.get('/url')
    assert response.status_code == 200
    data = response.json()
    assert 'url' in data
    assert 'http' in data['url']


def test_get_credit_card():
    response = client.get('/credit-card')
    assert response.status_code == 200
    data = response.json()
    assert 'provider' in data
    assert 'number' in data
    assert 'expire' in data
    assert 'security_code' in data


def test_get_user_agent():
    response = client.get('/user-agent')
    assert response.status_code == 200
    data = response.json()
    assert 'user_agent' in data


def test_get_all():
    response = client.get('/all')
    assert response.status_code == 200
    data = response.json()
    assert 'profile' in data
    assert 'full_name' in data
    assert 'address' in data
    assert 'email' in data
    assert 'job' in data
    assert 'text' in data
    assert 'ipv4' in data
    assert 'mac_address' in data
    assert 'phone_number' in data
    assert 'company' in data
    assert 'url' in data


def test_get_all_with_count():
    response = client.get('/all?count=2')
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert data['count'] == 2


def test_invalid_count():
    response = client.get('/name?count=0')
    assert response.status_code == 422


def test_count_exceeds_limit():
    response = client.get('/name?count=1000')
    assert response.status_code == 422
