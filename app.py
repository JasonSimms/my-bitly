# app.py
from flask import Flask, redirect, jsonify, request
from flask_restful import Api, Resource
from link_generator import generate_link


# Initialize the Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./fireBase_credentials.json")
firebase_admin.initialize_app(cred)

# Define the Firestore client
db = firestore.client()

print("lets gooooo")
app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["GET"])
def home():
    return "Welcome", 200


@app.route("/links", methods=["GET"])
def get_data():
    docs = db.collection("links").get()
    data = [doc.to_dict() for doc in docs]
    return jsonify(data), 200


@app.route("/new_link", methods=["POST"])
def add_link():
    print("add link")
    # Access the JSON body of the POST request
    data = request.get_json()
    generated_link = generate_link(data["name"])

    doc_ref = db.collection("links").document()
    write_result = doc_ref.set(generated_link)
    print(write_result)

    return (generated_link), 200


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    app.run(debug=True)


# class Quote(Resource):
#     def get(self, id=0):
#         if id == 0:
#             return random.choice(ai_quotes), 200
#         for quote in ai_quotes:
#             if(quote["id"] == id):
#                 return quote, 200
#         return "Quote not found", 404

# class Test(Resource):
#     def get(self):
#         print('redirection!')
#         return redirect("https://github.com/JasonSimms", code=302)
