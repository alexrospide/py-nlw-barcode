from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():
    print(request.json) # body da requisição http flask
    return jsonify({"resp": "OK"}), 200
