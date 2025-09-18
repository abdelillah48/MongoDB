# Mongo API - Gestion de clients

Petit projet pour tester **MongoDB**, **Mongo Express** et une **API Python Flask**.  
Il permet d'ajouter, lister et récupérer des clients via une API REST et de visualiser les données via Mongo Express.

## Prérequis

- Docker Desktop
- Python 3

## Installation

1. **Cloner et installer**
```bash
git clone <URL_DU_REPO>
cd mongo_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Lancer les services**
```bash
docker-compose up -d
python app.py
```

## Utilisation

- **API :** http://127.0.0.1:5000
- **Mongo Express :** http://localhost:8090 (webadmin / Pass@2025)

**Exemples de requêtes :**
```bash
# Ajouter un client
curl -X POST http://127.0.0.1:5000/clients -H "Content-Type: application/json" -d '{"nom":"Alice","email":"alice@email.com"}'

# Lister les clients
curl http://127.0.0.1:5000/clients

# Récupérer un client
curl http://127.0.0.1:5000/clients/<id>
```

## Arrêter

```bash
docker-compose down
```
