from flask import Blueprint, jsonify, request
from db import db
from models import ShoppingCart


# 创建名为 'shopping_cart' 的用户相关蓝图
shopping_cart = Blueprint('shopping_cart', __name__)


# 创建购物车商品
@shopping_cart.route('/api/shopping_cart', methods=['POST'])
def create_item():
    data = request.json
    new_item = ShoppingCart(
        type=data.get('type'),
        name=data['name'],
        unit=data.get('unit'),
        quantity=data.get('quantity', 0),
        user_id=data['user_id']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added to shopping cart successfully'})

# 获取所有购物车商品
@shopping_cart.route('/api/shopping_cart', methods=['GET'])
def get_all_items():
    items = ShoppingCart.query.all()
    items_json = []
    for item in items:
        items_json.append({
            'id': item.id,
            'type': item.type,
            'name': item.name,
            'unit': item.unit,
            'quantity': item.quantity,
            'user_id': item.user_id
        })
    return jsonify({'shopping_cart_items': items_json})

# 获取特定购物车商品
@shopping_cart.route('/api/shopping_cart/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = ShoppingCart.query.get(item_id)
    if item:
        item_json = {
            'id': item.id,
            'type': item.type,
            'name': item.name,
            'unit': item.unit,
            'quantity': item.quantity,
            'user_id': item.user_id
        }
        return jsonify({'shopping_cart_item': item_json})
    else:
        return jsonify({'error': 'Shopping cart item not found'}), 404

# 更新购物车商品
@shopping_cart.route('/api/shopping_cart/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = ShoppingCart.query.get(item_id)
    if not item:
        return jsonify({'error': 'Shopping cart item not found'}), 404
    data = request.json
    item.type = data.get('type', item.type)
    item.name = data.get('name', item.name)
    item.unit = data.get('unit', item.unit)
    item.quantity = data.get('quantity', item.quantity)
    item.user_id = data.get('user_id', item.user_id)
    db.session.commit()
    return jsonify({'message': f'Shopping cart item updated successfully for id {item_id}'})

# 删除购物车商品
@shopping_cart.route('/api/shopping_cart/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = ShoppingCart.query.get(item_id)
    if not item:
        return jsonify({'error': 'Shopping cart item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Shopping cart item deleted successfully for id {item_id}'})