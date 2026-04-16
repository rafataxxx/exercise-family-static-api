import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "¡Bienvenido a la API de la Familia Jackson!"}), 200

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/members', methods=['POST'])
def create_member():
    body = request.get_json()
    if not body:
        return jsonify({"error": "Bad request"}), 400
        
    new_member = jackson_family.add_member(body)
    return jsonify(new_member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_single_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)