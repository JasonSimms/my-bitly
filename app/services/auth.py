from dotenv import load_dotenv
from functools import wraps
import os
from flask import jsonify, request
import logging

load_dotenv()
API_KEY = os.getenv("API_KEY")

print("API_KEY", API_KEY)


def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        print(request.headers)
        provided_key = request.headers.get("Key")
        if provided_key and provided_key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            logging.error("bad key recieved!: " + str(provided_key))
            logging.error(request.args)
            message = "Invalid API Key: " + str(provided_key)
            return jsonify(error=message), 403

    return decorated_function
