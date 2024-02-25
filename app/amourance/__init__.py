from flask import Flask, render_template, request
import requests

API_TOKEN = "lqX09tlLKxyHeNVIO09wwsaW6XuowzG0e7SaY7bh"
url = 'http://127.0.0.1:5000/send'
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello(name=None):
        return render_template('hello.html', name=name)
    
    @app.route("/send", methods=['POST'])
    def send():
        ville = request.form['texte']
        date = request.form['date']
        response = requests.get(f"https://api.thenewsapi.com/v1/news/top?api_token=lqX09tlLKxyHeNVIO09wwsaW6XuowzG0e7SaY7bh&locale=fr&limit=1&language=fr&published_on={date}")
        if response.status_code == 200:
            json = response.json()
            titleNews = json.get('data')[0].get('title')
            urlNews = json.get('data')[0].get('url')
            return {'title': titleNews, 'url': urlNews}
        else:
            return {'error': 'Erreur lors de la récupération des données'}
    return app