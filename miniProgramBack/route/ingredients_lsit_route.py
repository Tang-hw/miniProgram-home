from flask import Blueprint, jsonify, request
from db import db
from models import IngredientsList

# 创建名为 'ingredients_list' 的用户相关蓝图
ingredients_list = Blueprint('ingredients_list', __name__)


@ingredients_list.route('/api/ingredients', methods=['POST'])
def create_ingredient():
    data = request.json
    new_ingredient = IngredientsList(
        name=data['name'],
        quantity=data['quantity'],
        unit=data['unit'],
        dish_id=data['dish_id']
    )
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({'message': 'Ingredient created successfully'})

# 获取所有配料条目
@ingredients_list.route('/api/ingredients', methods=['GET'])
def get_all_ingredients():
    ingredients = IngredientsList.query.all()
    ingredients_json = []
    for item in ingredients:
        ingredients_json.append({
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity,
            'unit': item.unit,
            'dish_id': item.dish_id
        })
    return jsonify({'ingredients': ingredients_json})

# 获取特定配料条目
@ingredients_list.route('/api/ingredients/<int:item_id>', methods=['GET'])
def get_ingredient(item_id):
    ingredient = IngredientsList.query.get(item_id)
    if ingredient:
        ingredient_json = {
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
            'dish_id': ingredient.dish_id
        }
        return jsonify({'ingredient': ingredient_json})
    else:
        return jsonify({'error': 'Ingredient not found'}), 404

# 更新配料条目
@ingredients_list.route('/api/ingredients/<int:item_id>', methods=['PUT'])
def update_ingredient(item_id):
    ingredient = IngredientsList.query.get(item_id)
    if not ingredient:
        return jsonify({'error': 'Ingredient not found'}), 404
    data = request.json
    ingredient.name = data.get('name', ingredient.name)
    ingredient.quantity = data.get('quantity', ingredient.quantity)
    ingredient.unit = data.get('unit', ingredient.unit)
    ingredient.dish_id = data.get('dish_id', ingredient.dish_id)
    db.session.commit()
    return jsonify({'message': f'Ingredient updated successfully for id {item_id}'})

# 删除配料条目
@ingredients_list.route('/api/ingredients/<int:item_id>', methods=['DELETE'])
def delete_ingredient(item_id):
    ingredient = IngredientsList.query.get(item_id)
    if not ingredient:
        return jsonify({'error': 'Ingredient not found'}), 404
    db.session.delete(ingredient)
    db.session.commit()
    return jsonify({'message': f'Ingredient deleted successfully for id {item_id}'})