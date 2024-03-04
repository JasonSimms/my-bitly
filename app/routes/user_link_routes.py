##### USER LINK ROUTES #####
from flask import Blueprint, jsonify, request
from app.services import require_api_key
import logging
import traceback

# from functools import wraps
from app.services import (
    generate_user_link,
    read_collection,
    create_record_with_id,
    require_api_key,
    delete_document_by_id,
)

user_link_bp = Blueprint("user_links", __name__)


@user_link_bp.route("/userlink", methods=["POST"])
@require_api_key
def add_user_link():
    return jsonify("BINGO"), 200
    # Access the JSON body of the POST request
    data = request.get_json()
    link_name = data["nickname"]
    link_url = data["url"]
    link_creator = data["creator"]

    user_link_record = generate_user_link(link_name, link_url, link_creator)
    doc_id = user_link_record["id"]

    # Add the generated link to the database
    write_result = create_record_with_id("user_links", doc_id, user_link_record)
    logging.info("User link added to the database")
    logging.info(write_result)

    # Add the link id to the user
    return (
        user_link_record
    ), 201  ##Front end can push to state and avoid another call to the db


@user_link_bp.route(
    "/userlink", methods=["DELETE"]
)  # TODO: this does not stop anyone with a credential from deleting any link
@require_api_key
def delete_user_link():
    # Access the JSON body of the POST request
    data = request.get_json()
    id = data["id"]
    result = delete_document_by_id("user_links", id)
    logging.info("User link deleted from the database: " + id)
    return (result), 204


@user_link_bp.route("/userlink", methods=["GET"])
def get_links():
    # Get the 'User-Id' from the request headers
    user_id = request.headers.get("User-Id")
    print("what is the user id?")
    print(len(user_id))
    print(user_id)

    # Read all documents from the 'user_links' collection
    all_user_links = read_collection("user_links")
    # Check if 'User-Id' is undefined

    if user_id is None or len(user_id) == 0:
        raise ValueError("User-Id is undefined in the request headers.")

    # Filter the documents to only include those where 'creator' matches the 'User-Id'
    filtered_user_links = [
        link for link in all_user_links if link.get("creator") == user_id
    ]

    # Sanitize the 'creator' key in each link
    sanitized_user_links = [
        {k: v for k, v in link.items() if k != "creator"}
        for link in filtered_user_links
    ]

    print(len(sanitized_user_links))

    # Return the filtered list of user links
    return jsonify(sanitized_user_links), 200
