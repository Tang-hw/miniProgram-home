from flask import Blueprint, jsonify, request
from db import db
from models import DishSquare

# 创建名为 'dish_square' 的用户相关蓝图
dish_square = Blueprint('dish_square', __name__)

# 查询所有
@dish_square.route('/api/dish_square', methods=['GET'])
def get_dish_square():
    dish_square = DishSquare.query.all()
    result = [{'id': d.id, 'dish_id': d.dish_id, 'author_id': d.author_id, 'hotness': d.hotness} for d in dish_square]
    return jsonify({'dish_square': result})

# 新增
@dish_square.route('/api/dish_square', methods=['POST'])
def add_dish_square():
    data = request.json
    new_dish_square = DishSquare(dish_id=data['dish_id'], author_id=data['author_id'], hotness=data.get('hotness', 0))
    db.session.add(new_dish_square)
    db.session.commit()
    return jsonify({'message': 'Dish square added successfully'})

# 更新一条记录
@dish_square.route('/api/dish_square/<int:id>', methods=['PUT'])
def update_dish_square(id):
    data = request.json
    dish_square = DishSquare.query.get(id)
    if not dish_square:
        return jsonify({'error': 'Dish square not found'}), 404
    dish_square.dish_id = data.get('dish_id', dish_square.dish_id)
    dish_square.author_id = data.get('author_id', dish_square.author_id)
    dish_square.hotness = data.get('hotness', dish_square.hotness)
    db.session.commit()
    return jsonify({'message': f'Dish square updated successfully for id {id}'})

# 删除一条记录
@dish_square.route('/api/dish_square/<int:id>', methods=['DELETE'])
def delete_dish_square(id):
    dish_square = DishSquare.query.get(id)
    if not dish_square:
        return jsonify({'error': 'Dish square not found'}), 404
    db.session.delete(dish_square)
    db.session.commit()
    return jsonify({'message': f'Dish square deleted successfully for id {id}'})