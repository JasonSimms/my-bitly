# app.py
from flask import Flask, redirect, jsonify, request
from flask_restful import Api, Resource
from recipient_generator import generate_recipient
from link_generator import generate_link
from firestore_CRUD import create_record, read_collection, create_record_with_id

print("lets gooooo")
app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["GET"])
def home():
    return "Welcome", 200


@app.route("/links", methods=["GET"])
def get_links():
    data = read_collection("links")
    return (data), 200


@app.route("/new_link", methods=["POST"])
def add_link():
    # Access the JSON body of the POST request
    data = request.get_json()
    link_record = generate_link(data["name"], data["url"])

    # Add the generated link to the database
    write_result = create_record("links", link_record)
    print(write_result)

    return (link_record), 201


@app.route("/recipients", methods=["GET"])
def get_recipients():
    data = read_collection("recipients")
    return (data), 200


@app.route("/new_recipient", methods=["POST"])
def add_recipient():
    # Access the JSON body of the POST request
    data = request.get_json()
    recipient = generate_recipient(data["name"])
    doc_id = recipient["name"].strip().lower()

    # Add the generated link to the database
    write_result = create_record_with_id("recipients", "blaaa", doc_id)
    return (write_result), 201


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
