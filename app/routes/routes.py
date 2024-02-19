from flask import Flask, redirect, jsonify, request, Blueprint
from flask_restful import Api, Resource
from app.services.recipient_generator import generate_recipient
from app.services.link_generator import generate_link
from app.services.firestore_CRUD import (
    create_record,
    read_collection,
    create_record_with_id,
    find_document_by_id,
)


bp = Blueprint("links", __name__)

# @bp.route('/links')
# def get_links():
#     # Your code here
#     return('bingo')
#     pass


@bp.route("/", methods=["GET"])
def home():
    return "Welcome", 200


@bp.route("/links", methods=["GET"])
def get_links():
    data = read_collection("links")
    return (data), 200


@bp.route("/new_link", methods=["POST"])
def add_link():
    # Access the JSON body of the POST request
    data = request.get_json()
    link_record = generate_link(data["name"], data["url"])

    # Add the generated link to the database
    write_result = create_record("links", link_record)
    print(write_result)

    return (link_record), 201


@bp.route("/recipients", methods=["GET"])
def get_recipients():
    data = read_collection("recipients")
    return (data), 200


@bp.route("/new_recipient", methods=["POST"])
def add_recipient():
    # Access the JSON body of the POST request
    data = request.get_json()
    recipient = generate_recipient(data["name"])
    doc_id = recipient["name"].strip().lower()

    # Add the generated link to the database
    write_result = create_record_with_id("recipients", "blaaa", doc_id)
    return (write_result), 201


@bp.route("/mylink/<string:link_name>/<string:recipient>", methods=["GET"])
def redirect_link(link_name, recipient):
    # obj = { "link_name": link_name, "recipient": recipient }
    # return(obj)
    # look up the link
    myDoc = find_document_by_id("links", link_name)
    return myDoc
    # return redirect("https://github.com/JasonSimms", code=302)


@bp.route("/", defaults={"path": ""})
@bp.route("/<path:path>")
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404
