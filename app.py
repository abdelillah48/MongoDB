from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://admin_user:SuperSecret123@localhost:28018/")
db = client["ma_base"]
clients_collection = db["clients"]

# Ajouter un client
@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json
    if not data.get("nom") or not data.get("email"):
        return jsonify({"error": "nom et email requis"}), 400
    result = clients_collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)}), 201

# Lister tous les clients
@app.route("/clients", methods=["GET"])
def get_clients():
    clients = []
    for client_doc in clients_collection.find():
        client_doc["_id"] = str(client_doc["_id"])
        clients.append(client_doc)
    return jsonify(clients)

# Récupérer un client par id
@app.route("/clients/<id>", methods=["GET"])
def get_client(id):
    client_doc = clients_collection.find_one({"_id": ObjectId(id)})
    if client_doc:
        client_doc["_id"] = str(client_doc["_id"])
        return jsonify(client_doc)
    else:
        return jsonify({"error": "Client non trouvé"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
