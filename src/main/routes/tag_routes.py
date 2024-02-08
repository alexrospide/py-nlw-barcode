from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():
    tag_creator_view = TagCreatorView()

# mexi aqui para validar o parametro incorreto
    only_request_json = request.json
    if "product_code" in only_request_json:
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)

        return jsonify(response.body), response.status_code

    return jsonify({"erro":"Incorrect Paramiter"}), 404
