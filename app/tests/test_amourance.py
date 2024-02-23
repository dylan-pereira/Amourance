def test_home_page(client):
    response = client.get("/")
    assert b"<p>Hello, World!</p>" in response.data
