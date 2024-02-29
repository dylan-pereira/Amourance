# Amourance
## Consignes
### Générales:
2 à 3 personnes
Développement d’une webapp faisant appel à une ou plusieurs api externes. Le sujet de la web app est libre.
2 à 3 end user features (1 par personne)
Ecriture de  tests pour chacune de vos features.
Écriture d’un Dockerfile.
Ecriture de documentation (What is it, what service/feature it can provide, how to build, how to test, how to run locally)

### Ecriture de la CI:
Github Actions
Doit supporter un "Scaled Trunk-Based Development" branching pattern
Le code doit être testé dans la CI
Le code ne passant pas les tests ne doit pas être buildé
Le code passant les tests est “dockerisé”, taggued et pushed en fonction du type de build.

Une publication de l’image docker en fonction d’une github release est prise en charge par la CI

### Runtime:
Si une clé d’API est nécessaire pour l’utilisation de votre webapp, ne la bakez pas à l'intérieur de l’image, mais passer là au runtime du container.

### Communiquez moi la clé d’api à utiliser via Discord en privé si nécessaire.
Liste d'Apis publiques:
https://github.com/public-apis/public-apis

## Sujet choisi
Nom: Amourance
Repo Github: https://github.com/dylan-pereira/Amourance

Fonctionnalitées:
Input de Ville + date
On récupère la tempéature de la ville (https://api.api-ninjas.com/v1/weather)
On affiche une blague (https://api.api-ninjas.com/v1/jokes)
On affiche un news du jour (https://api.thenewsapi.com/v1/news/top)

Membres:
Clément Lamoine @LAMOANE 
Dylan Pereira @Dylann 
Samuel Ohayon @samom13584 


## Documentation

### What is it?
Amourance est une application web conçue pour offrir une expérience unique et personnalisée en fonction de la ville et de la date choisies par l'utilisateur. En entrant ces informations, l'application récupère et présente des données telles que la météo locale, une blague pour égayer la journée et une actualité du jour pour tenir l'utilisateur informé. Cette combinaison de fonctionnalités vise à créer une expérience quotidienne agréable et engageante, tout en fournissant des informations utiles et divertissantes.
### What service/feature it can provide?
1. Météo Locale: Amourance utilise une API externe pour récupérer les informations météorologiques de la ville spécifiée par l'utilisateur. Cela permet aux utilisateurs de planifier leur journée en connaissant à l'avance les conditions météorologiques, telles que la température, les précipitations, le vent, etc.

2. Blague du Jour: Pour ajouter une touche de légèreté et de divertissement, l'application affiche une blague aléatoire récupérée grâce à une API dédiée aux blagues. Cela vise à améliorer l'humeur de l'utilisateur et à offrir un moment de détente.

3. Actualité du Jour: Amourance intègre également une fonctionnalité d'actualités en se connectant à une API d'actualités pour fournir une nouvelle pertinente et actuelle. Cela permet aux utilisateurs de rester informés des événements importants et des dernières nouvelles du monde entier ou de leur région, selon les paramètres de l'API.

En combinant ces services, Amourance offre une expérience utilisateur riche et variée, rendant chaque interaction à la fois informative et divertissante.
### How to setup?
Remplacer `api_token` par les tokens correspondant des API. 

    echo -e "API_TOKEN_NEWS=api_token\nAPI_TOKEN_NINJA=api_token" > .env

### How to build?
    docker compose build

L'image sera taggé de cette manière : `amourance:latest`
### How to test?
    docker compose run --rm web-app pytest
### How to run locally?
    docker compose up -d

La web app est disponible [ici](http://localhost:8080).