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
On récupère la météo de la ville (https://api-ninjas.com/api/weather)
On affiche l'horoscope du jour (https://aztro.readthedocs.io/en/latest/)
On affiche un news du jour (https://www.thenewsapi.com/documentation)

Membres:
Clément Lamoine @LAMOANE 
Dylan Pereira @Dylann 
Samuel Ohayon @samom13584 


## Documentation

### What is it?
### What service/feature it can provide?
### How to build?
### How to test? 
### How to run locally?
