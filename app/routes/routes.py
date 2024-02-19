from flask import Flask, redirect, jsonify, request, Blueprint, render_template
from flask_restful import Api, Resource
from app.services import (
    generate_recipient,
    generate_link,
    create_record,
    read_collection,
    create_record_with_id,
    find_document_by_id,
)


bp = Blueprint("links", __name__)


@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@bp.route("/links", methods=["GET"])
def get_links():
    data = read_collection("links")
    return (data), 200


@bp.route("/new_link", methods=["POST"])
def add_link():
    # Access the JSON body of the POST request
    data = request.get_json()
    link_name = data["name"]
    link_url = data["url"]

    link_record = generate_link(link_name, link_url)
    doc_id = link_record["id"]

    # if not isinstance(link_record, dict) or "name" not in link_record or "url" not in link_record:
    #     raise ValueError("Generated link is not a valid object with 'name' and 'url' keys")

    # Add the generated link to the database
    write_result = create_record_with_id("links", doc_id, link_record)
    return (jsonify(write_result)), 201


@bp.route("/recipients", methods=["GET"])
def get_recipients():
    data = read_collection("recipients")
    return (data), 200


@bp.route("/foo", methods=["GET"])
def do_foo():
    recipients = read_collection("recipients")
    recipient_ids = [recipient["id"] for recipient in recipients]
    links = read_collection("links")
    links = [link["id"] for link in links]

    recipient_links = []
    for x in recipient_ids:
        obj = {"recipient": x}
        for y in links:
            print("link", x, y)
            obj[y] = x + "/" + y
            # recipient_links.append(x+'/'+y)
        recipient_links.append(obj)

    return (jsonify(recipient_links)), 200


@bp.route("/new_recipient", methods=["POST"])
def add_recipient():
    # Access the JSON body of the POST request
    data = request.get_json()
    recipient_name = data["name"]
    recipient = generate_recipient(recipient_name)
    doc_id = recipient["id"]

    # Add the generated link to the database
    write_result = create_record_with_id("recipients", doc_id, recipient)
    return (jsonify(write_result)), 201


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

# @bp.errorhandler(Exception)
# def handle_error(e):
#         print('myError',e)
#         return jsonify({"error": str(e)}), 500


def catch_all(path):
    return jsonify({"error": "Not Found"}), 404
