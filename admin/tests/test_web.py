from web import create_app

app = create_app()
app.testing = True
client = app.test_client()


def test_home():
    response = client.get("/")
    assert b"Hola Mundo" in response.data