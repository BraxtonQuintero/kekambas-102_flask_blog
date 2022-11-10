from flask import jsonify, request
from . import api
from app.models import Post


@api.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@api.route('/users/<user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify([user.to_dict()])



@api.route('/users/', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({'error', "Your request content type must be application/json"}), 400
    data = request.json
    print(data)
    print(type(data))
    for field in ['email', 'username', 'password']:
        if field not in data:
            return jsonify({"error": f"'{field}' must be in request body"}), 400

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    print(email, username, password)
    new_user = User(email=email, username=username, password=password)
    return jsonify(new_user.to_dict()), 201


    