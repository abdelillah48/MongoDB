# Mongo API - Gestion de clients

Petit projet pour tester **MongoDB**, **Mongo Express** et une **API Python Flask**.  
Il permet d'ajouter, lister et récupérer des clients via une API REST et de visualiser les données via Mongo Express.

## Prérequis

- Docker Desktop installé et lancé
- Python 3 et pip

## Structure du projet

```
mongo_api/
│
├── docker-compose.yml
├── app.py
└── requirements.txt
```

## Étapes complètes pour exécuter le projet

### 1. Cloner le projet

```bash
git clone <URL_DU_REPO>
cd mongo_api
```

### 2. Créer un environnement virtuel Python et l'activer

```bash
python3 -m venv venv
source venv/bin/activate
```

Tu devrais voir `(venv)` dans le terminal, ce qui indique que l'environnement est actif.

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Installe Flask, PyMongo et dnspython dans l'environnement virtuel.

### 4. Lancer MongoDB et Mongo Express avec Docker Compose

```bash
docker-compose up -d
```

- **MongoDB accessible sur :** `localhost:28018`
- **Mongo Express accessible sur :** http://localhost:8090
  - **Username :** `webadmin`
  - **Password :** `Pass@2025`
  - **Base :** `ma_base`
  - **Collection :** `clients`

Vérifier les conteneurs :

```bash
docker ps
```

### 5. Lancer l'API Python

```bash
python app.py
```

L'API sera disponible sur : http://127.0.0.1:5000

## Tester l'API

### Ajouter un client

```bash
curl -X POST http://127.0.0.1:5000/clients \
-H "Content-Type: application/json" \
-d '{"nom":"Alice","email":"alice@email.com"}'
```

### Lister tous les clients

```bash
curl http://127.0.0.1:5000/clients
```

### Récupérer un client par ID

```bash
curl http://127.0.0.1:5000/clients/<id_client>
```

## Visualiser les données avec Mongo Express

1. Ouvrir dans le navigateur : http://localhost:8090
2. **Base :** `ma_base`
3. **Collection :** `clients`

Tu verras tous les clients ajoutés via l'API.

## Arrêter les services

```bash
docker-compose down
```

Pour supprimer complètement les volumes (perte de toutes les données) :

```bash
docker-compose down -v
```
