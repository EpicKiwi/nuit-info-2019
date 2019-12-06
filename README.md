# Projet principal Nuit de l'info 2019 : No PLS

> Projet principal de la nuit de l'info 2019 dit No PLS

## Intro

Le but de ce défi était de créer un outil permettant aux étudiants "novices" de profiter de l'expérience et des conseils d'étudiants plus expérimentés. 

## Vision du sujet

- Identification des ressources
- Mise en relation pair à pair

L'application web est **collaborative**. 
Chacun peut poster un "guide" sur une démarche administrative, scolaire... qu'il a pu expérimenter et qu'il souhaiterait **partager avec autrui**. 

L'application permet de voir les démarches, divisées en étapes, en bas désquelles chacun peut ajouter un commentaire, afin de rajouter sa pierre à l'édifice.

## Utilisation de l'application

1. La page d'accueil affiche la liste des **dernières procédures**. Une barre de recherche permet de trouver plus simplement sa procédure.
2. La procédure est composée d'une **suite d'actions**. Pour chacune, on a un texte explicatif, une durée approximative, si elle peut être faite en physique ou online (avec les informations necessaires), et les documents qui peuvent être liées. Sous chacune, les commentaires les plus utiles (votés par la communauté) sont affichés. 
3. Une fois toutes les étapes terminées, l'utilisateur gagne un **point de procédure** et il peut devenir **Helper** pour l'article ! Cela permettra à d'autres usagers de lui envoyer un message concernant cette démarche.

*Visuel de l'application*
![Visuel de l'application](https://cdn.discordapp.com/attachments/652190133176500256/652376458597105695/20191206_061034.jpg "Visuel de l'application")*ouvrez l'image dans un nouvel onglet si vous la voulez à l'endroit*

## Accès au code

* [Version live](https://nopls.epickiwi.fr/)


## Installation

Assurez vous d'avoir installé Python *3.x* et qu'il est accessible sur la commande `python`.

Clonez le repository

```
git clone git@github.com:EpicKiwi/nuit-info-2019.git
```

Installez les dépendances

```
pip install -r src/requirements.txt
```

Démarrez le serveur

```
./dev.sh runserver
```

**OU** Démarrez la configuration `Dev` dans Pycharm

## Migrations

Executez les migration de la base de données

```
./dev.sh migrate
```

## Déploiement Docker

La solution peut complètement être déployée avec Docker. Nous avons prévue 2 images Docker.

### Prérequis

La solution nécéssite le déploiement d'une base de données Postgres SQL. Elle peut être déployée avec docker comms suit :

```
docker run -v /var/pg-data:/var/lib/postgresql/data --name pg-no-pls postgres
```

### Espace de stockage

La solution nécéssite 2 volumes persistant permettant de contenir les fichiers statiques ainsi que les fichiers envoyés par les utilisateurs.

On peut créer ces deux volumes comme suit :

```
docker create volume media-files
docker create volume static-files
```

### Configuration de la solution

Sur le déploiement Django et Postgres, il conviens de renseigner les variables d'environnement suivantes

```
# Nom de la base de données
POSTGRES_DB=nopls
# Nom d'utilisateur de la base de données
POSTGRES_USER=nopls
# Mot de passe de l'utilisateur postgres
POSTGRES_PASSWORD=mypostgrespasswd
# Clé secrete Django
SECRETKEY=mydjangosecret
```

### Déploiement de la solution Django

Dans un premier temps, il faut construire l'image située dans ce repository

```
docker build . -t -e POSTGRES_DB=nopls -e POSTGRES_USER=nopls -e POSTGRES_PASSWORD=mypostgrespasswd cesimmortel/nopls-django
```

On peut alors déployer la solution comme suit :

```
docker run -e POSTGRES_HOST=pg-no-pls -e POSTGRES_DB=nopls -e POSTGRES_USER=nopls -e POSTGRES_PASSWORD=mypostgrespasswd -e SECRETKEY=mydjangosecret -v user-media:/var/media -v static-files:/var/static cesimmortel/nopls-django
```

### Reverse proxy

Il faut ensuite construire et démarrer le serveur reverse proxy qui est en charge de servir les données statiques et Django.

```
docker build proxy -t cesimmortel/nopls-proxy
```

Et le démarrer comme suit :

```
docker run -v user-media:/var/media -v static-files:/var/static cesimmortel/nopls-proxy
```

### Docker compose

Pour votre installation, nous préconisons l'utilisation de Docker compose. Vous pouvez vous inspirer du fichier que nous avons utilisé pour le déploiement en production.