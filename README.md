# Projet principal Nuit de l'info 2019 : No PLS

> Projet principal de la nuit de l'info 2019 dit No PLS

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