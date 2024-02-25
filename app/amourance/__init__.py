from flask import Flask, render_template, request
import requests
import os

API_TOKEN_NEWS = os.environ.get('API_TOKEN_NEWS')
API_TOKEN_NINJA = os.environ.get('API_TOKEN_NINJA')

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/send_and_show", methods=['POST'])
    def send_and_show():
        response = send()
        return render_template('home.html', response=response)

    
    @app.route("/send", methods=['POST'])
    def send():
        ville = request.form['ville']
        date = request.form['date']

        # Appel à l'API pour les news
        response = requests.get(f"https://api.thenewsapi.com/v1/news/top?api_token={API_TOKEN_NEWS}&locale=fr&limit=1&language=fr&published_on={date}")
        if response.status_code == 200:
            json = response.json()
            titleNews = json.get('data')[0].get('title')
            urlNews = json.get('data')[0].get('url')
        else:
            return {'error': 'Erreur lors de la récupération des données des news'}

        # Appel à l'API pour la météo
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(ville)
        weather_response = requests.get(api_url, headers={'X-Api-Key': API_TOKEN_NINJA})
        if weather_response.status_code == 200:
            weather_json = weather_response.json()
            temperature = weather_json.get('temp')
        else:
            return {'error': 'Erreur lors de la récupération des données de météo'}

        # Appel à l'API pour la joke
        limit = 1
        api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
        joke_response = requests.get(api_url, headers={'X-Api-Key': API_TOKEN_NINJA})
        if joke_response.status_code == 200:
            joke_json = joke_response.json()
            joke = joke_json[0].get('joke')
        else:
            return {'error': 'Erreur lors de la récupération de la blagounette'}

        return {'title': titleNews, 'url': urlNews, 'temperature': temperature, "joke": joke}
    return app