from dotenv import load_dotenv
from functools import wraps
import os
from flask import jsonify, request
import logging
from firebase_admin import auth

# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# print("API_KEY", API_KEY)


def validate_token(token):
    print("toke:", token)
    if token.startswith("Bearer "):
        token = token[7:]
    try:
        decoded_token = auth.verify_id_token(token)
        # uid = decoded_token['uid']
        print(f"Decoded token: {decoded_token}")
        # print(f"User ID: {uid}")
        # return uid
        return True
    except (auth.InvalidIdTokenError, ValueError) as e:
        print(f"Error: {e}")
        return None


def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        print("require_authorization init")
        # logging.info(request.headers)
        provided_key = request.headers.get("authorization")
        # or request.headers.get("Key")
        # return view_function(*args, **kwargs)
        if not provided_key:
            logging.error("no key recieved!")
            message = "No API Key provided"
            return jsonify(error=message), 403
        test = validate_token(provided_key)
        print(f"User ID: {test}")
        return ("BINGO", 200)
        # if provided_key  == API_KEY:
        #     return view_function(*args, **kwargs)
        # else:
        #     logging.error("bad key recieved!: " + str(provided_key))
        #     logging.error(request.args)
        #     message = "Invalid API Key: " + str(provided_key)
        #     return jsonify(error=message), 403

    return decorated_function


def list_all_users():  #TODO remove this
    print("lets get users")
    # Start listing users from the beginning, 1000 at a time.
    try:
        page = auth.list_users()
        while page:
            for user in page.users:
                print('User: ' + user.email)
            # Get next batch of users.
            page = page.get_next_page()
    except Exception as e:
        print("Error listing users: " + str(e))
        return


# Call the function to list all users
# list_all_users()
