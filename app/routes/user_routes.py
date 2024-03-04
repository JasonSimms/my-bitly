##### USER ROUTES #####
from flask import Blueprint, jsonify, request
from app.services import require_api_key
import logging
from app.services import create_record_with_id
from app.services import list_all_users

user_bp = Blueprint("user", __name__)


@user_bp.route("/user", methods=["GET"])
def debug_user():
    try:
        list_all_users()
    except Exception as e:
        logging.error("handle_error!!!!!!!!!!!!!!!", e)
        # return jsonify({"error": str(e)}), 500
    return jsonify(["user1", "user2", "user3"])


@user_bp.route("/user", methods=["POST"])
@require_api_key
def add_user():
    # Access the JSON body of the POST request
    data = request.get_json()
    print("wooo")
    # print all keys of data
    print(data.keys())
    id = data["uid"]
    email = data["email"]
    displayName = data.get("displayName", email)
    photoUrl = data.get("photoUrl", None)  # TODO add fallback image avatar

    user_record = {
        "id": id,
        "displayName": displayName,
        "email": email,
        "photoUrl": photoUrl,
    }

    # Add the generated user to the DB
    write_result = create_record_with_id("users", id, user_record)
    logging.info("User added to the database")

    # # Add the link id to the user
    return (
        jsonify(write_result)
    ), 201  ##Front end can push to state and avoid another call to the db
