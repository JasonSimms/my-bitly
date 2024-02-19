# app.py
from flask import Flask, redirect
from flask_restful import Api, Resource
from quotes import ai_quotes
import random

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
        print('redicection!')
        return redirect("https://github.com/JasonSimms", code=302)
    
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
api.add_resource(Test, "/test", "/test/")

if __name__ == '__main__':
    app.run(debug=True)