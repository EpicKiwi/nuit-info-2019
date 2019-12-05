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
./dev.sh
```

**OU** Démarrez la configuration `Dev` dans Pycharm

## Migrations

Executez les migration de la base de données

```
cd src/ && python manage.py migrate
```