# app.py
from flask import Flask, redirect, jsonify
from flask_restful import Api, Resource
from quotes import ai_quotes
import random



# Initialize the Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./fireBase_credentials.json")
firebase_admin.initialize_app(cred)

# Define the Firestore client
db = firestore.client()

print('lets gooooo')
app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404
    
class Test(Resource):
    def get(self):
        print('redirection!')
        return redirect("https://github.com/JasonSimms", code=302)

class DBRead(Resource):
    def get(self):
        print('db read!')
        return "DB Read", 200
    
@app.route('/get_data', methods=['GET'])
def get_data():
       docs = db.collection('links').get()
       data = [doc.to_dict() for doc in docs]
       return jsonify(data),  200
    
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
api.add_resource(Test, "/test", "/test/")
api.add_resource(DBRead, "/test2", "/test2/")


if __name__ == '__main__':
    app.run(debug=True)