from flask import Blueprint, jsonify, request
from db import db
from models import UserInfo


# 创建名为 'user_info' 的用户相关蓝图
user_info = Blueprint('user_info', __name__)

# 创建用户
@user_info.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = UserInfo(
        name=data['name'],
        description=data.get('description'),
        photo=data.get('photo')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

# 获取所有用户
@user_info.route('/api/users', methods=['GET'])
def get_all_users():
    users = UserInfo.query.all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'name': user.name,
            'description': user.description,
            'recipe_count': user.recipe_count,
            'like_count': user.like_count,
            'photo': user.photo
        })
    return jsonify({'users': users_json})

# 获取特定用户
@user_info.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserInfo.query.get(user_id)
    if user:
        user_json = {
            'id': user.id,
            'name': user.name,
            'description': user.description,
            'recipe_count': user.recipe_count,
            'like_count': user.like_count,
            'photo': user.photo
        }
        return jsonify({'user': user_json})
    else:
        return jsonify({'error': 'User not found'}), 404

# 更新用户信息
@user_info.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = UserInfo.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    user.name = data.get('name', user.name)
    user.description = data.get('description', user.description)
    user.photo = data.get('photo', user.photo)
    db.session.commit()
    return jsonify({'message': f'User updated successfully for id {user_id}'})

# 删除用户
@user_info.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserInfo.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User deleted successfully for id {user_id}'})