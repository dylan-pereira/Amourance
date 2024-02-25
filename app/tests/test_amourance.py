def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_send_endpoint(client):
    response = client.post('/send', data={'ville': 'Paris', 'date': '2024-02-24'})
    assert response.status_code == 200
    assert b"temperature" in response.data
    assert b"title" in response.data
    assert b"url" in response.data
    assert b"joke" in response.data

def test_invalid_date_format(client):
    response = client.post('/send', data={'ville': 'Paris', 'date': '24/02/2024'})
    assert response.status_code == 200
    assert b"error" in response.data

def test_invalid_date_format_letter(client):
    response = client.post('/send', data={'ville': 'Paris', 'date': 'azdgazd'})
    assert response.status_code == 200
    assert b"error" in response.data

def test_missing_city(client):
    response = client.post('/send', data={'date': '2024-02-24'})
    assert response.status_code == 400

def test_missing_date(client):
    response = client.post('/send', data={'ville': 'Paris'})
    assert response.status_code == 400

def test_invalid_city(client):
    response = client.post('/send', data={'ville': 'VilleInexistante', 'date': '2024-02-24'})
    assert response.status_code == 200
    assert b"error" in response.data

def test_invalid_city_and_date(client):
    response = client.post('/send', data={'ville': 'VilleInexistante', 'date': '24/02/2024'})
    assert response.status_code == 200
    assert b"error" in response.data

def test_invalid_city_valid_date(client):
    response = client.post('/send', data={'ville': 'VilleInexistante', 'date': '2024-02-24'})
    assert response.status_code == 200
    assert b"error" in response.data

def test_valid_city_invalid_date(client):
    response = client.post('/send', data={'ville': 'Paris', 'date': '24/02/2024'})
    assert response.status_code == 200
    assert b"error" in response.data
