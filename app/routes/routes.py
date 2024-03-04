from flask import Flask, redirect, jsonify, request, Blueprint, render_template
import logging
import traceback
from functools import wraps
from app.services import (
    generate_recipient,
    generate_user_link,
    create_record,
    read_collection,
    create_record_with_id,
    find_document_by_id,
    find_document,
    generate_click_record,
    update_link_clicks,
    generate_deliverable_links,
    require_api_key,
    delete_document_by_id,
)

from .user_routes import user_bp


bp = Blueprint("links", __name__)


@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# @bp.route("/userlink", methods=["DELETE"])  #TODO: this does not stop anyone with a credential from deleting any link
# @require_api_key
# def delete_user_link():
#     # Access the JSON body of the POST request
#     data = request.get_json()
#     id = data["id"]
#     result = delete_document_by_id("user_links", id)
#     return (result), 204

# @bp.route("/userlink", methods=["GET"])
# def get_links():
#     data = read_collection("user_links")
#     return (data), 200


##### CAMPAIGN ROUTES #####
# @bp.route("/userlink", methods=["POST"])
# @require_api_key
# def add_user_link():
#     # Access the JSON body of the POST request
#     data = request.get_json()
#     link_name = data["name"]
#     link_url = data["url"]

#     user_link_record = generate_user_link(link_name, link_url)
#     doc_id = user_link_record["id"]

#     # Add the generated link to the database
#     write_result = create_record_with_id("user_links", doc_id, user_link_record)
#     return (jsonify(user_link_record)), 201  ##Front end can push to state and avoid another call to the db

# @bp.route("/userlink", methods=["DELETE"])  #TODO: this does not stop anyone with a credential from deleting any link
# @require_api_key
# def delete_user_link():
#     # Access the JSON body of the POST request
#     data = request.get_json()
#     id = data["id"]
#     result = delete_document_by_id("user_links", id)
#     return (result), 204

# @bp.route("/campaign", methods=["GET"])
# def get_links():
#     data = read_collection("user_links")
#     return (data), 200


# @bp.route("/new_link", methods=["POST"])
# @require_api_key
# def add_link():
#     # Access the JSON body of the POST request
#     data = request.get_json()
#     link_name = data["name"]
#     link_url = data["url"]

#     user_link_record = generate_user_link(link_name, link_url)
#     doc_id = user_link_record["id"]

#     # if not isinstance(link_record, dict) or "name" not in link_record or "url" not in link_record:
#     #     raise ValueError("Generated link is not a valid object with 'name' and 'url' keys")

#     # Add the generated link to the database
#     write_result = create_record_with_id("user_links", doc_id, user_link_record)
#     return (jsonify(write_result)), 201


@bp.route("/recipients", methods=["GET"])
def get_recipients():
    data = read_collection("recipients")
    return (data), 200


@bp.route("/deliverablelinks", methods=["GET"])
def get_deliverable_links():
    # read the recipients and links
    recipients = read_collection("recipients")
    recipient_ids = [recipient["id"] for recipient in recipients]
    links = read_collection("links")
    links = [link["id"] for link in links]

    # generate the deliverable links
    base_url = request.url_root
    recipient_links = generate_deliverable_links(recipient_ids, links, base_url)

    return (jsonify(recipient_links)), 200


@bp.route("/new_recipient", methods=["POST"])
@require_api_key
def add_recipient():
    # Access the JSON body of the POST request
    data = request.get_json()
    recipient_name = data["name"]
    recipient = generate_recipient(recipient_name)
    doc_id = recipient["id"]

    # Add the generated link to the database
    write_result = create_record_with_id("recipients", doc_id, recipient)
    return (jsonify(write_result)), 201


@bp.route("/mylink/<string:link_name>", methods=["GET"])
def redirect_link(link_name):
    tracker_id = request.args.get("id", default=None, type=str)

    # look up the link
    myDoc = find_document_by_id("links", link_name)
    if not myDoc:
        message = (
            "Link not found link_name: " + link_name + " tracker_id: " + tracker_id
        )
        logging.error(message, exc_info=True)
        return redirect("https://github.com/JasonSimms", code=302)

    # log the click:
    click_record = generate_click_record(tracker_id)
    update_result = update_link_clicks(myDoc["id"], click_record)
    print(update_result)

    # redirect to the link
    target = myDoc["url"]
    if not target:
        message = (
            "Link not found  myDoc[url]: "
            + jsonify(myDoc)
            + " tracker_id: "
            + tracker_id
        )
        logging.error(message, exc_info=True)
        return redirect("https://github.com/JasonSimms", code=302)
    return redirect(target, code=302)


@bp.route("/debug", methods=["GET"])
@require_api_key
def debug():
    base_url = request.url_root
    return jsonify("base_url: " + base_url)


# @bp.route("/", defaults={"path": ""})
# @bp.route("/<path:path>")


@bp.errorhandler(Exception)
def handle_error(e):
    # print('myError',e)
    stack_trace = traceback.format_exc()
    logging.error("handle_error", e, stack_trace)
    return jsonify({"error": str(e)}), 500


def catch_all(path):
    return jsonify({"error": "Not Found"}), 404
