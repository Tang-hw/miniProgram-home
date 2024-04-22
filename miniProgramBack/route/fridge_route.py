from flask import Blueprint, jsonify, request
from db import db
from models import Fridge

# 创建名为 'fridge' 的用户相关蓝图
fridge = Blueprint('fridge', __name__)

# 创建冰箱条目
@fridge.route('/api/fridge', methods=['POST'])
def create_fridge_item():
    data = request.json
    new_fridge_item = Fridge(
        type=data.get('type'),
        name=data.get('name'),
        quantity=data.get('quantity', 0),
        currency=data.get('currency'),
        price=data.get('price'),
        expiry_days=data.get('expiry_days'),
        expiry_date=data.get('expiry_date'),
        photo=data.get('photo'),
        user_id=data.get('user_id')
    )
    db.session.add(new_fridge_item)
    db.session.commit()
    return jsonify({'message': 'Fridge item created successfully'})

# 获取所有冰箱条目
@fridge.route('/api/fridge', methods=['GET'])
def get_all_fridge_items():
    fridge_items = Fridge.query.all()
    fridge_items_json = []
    for item in fridge_items:
        fridge_items_json.append({
            'id': item.id,
            'type': item.type,
            'name': item.name,
            'quantity': item.quantity,
            'currency': item.currency,
            'price': str(item.price) if item.price is not None else None,
            'expiry_days': item.expiry_days,
            'expiry_date': str(item.expiry_date) if item.expiry_date is not None else None,
            'photo': item.photo,
            'user_id': item.user_id
        })
    return jsonify({'fridge_items': fridge_items_json})

# 获取特定冰箱条目
@fridge.route('/api/fridge/<int:item_id>', methods=['GET'])
def get_fridge_item(item_id):
    item = Fridge.query.get(item_id)
    if item:
        item_json = {
            'id': item.id,
            'type': item.type,
            'name': item.name,
            'quantity': item.quantity,
            'currency': item.currency,
            'price': str(item.price) if item.price is not None else None,
            'expiry_days': item.expiry_days,
            'expiry_date': str(item.expiry_date) if item.expiry_date is not None else None,
            'photo': item.photo,
            'user_id': item.user_id
        }
        return jsonify({'fridge_item': item_json})
    else:
        return jsonify({'error': 'Fridge item not found'}), 404

# 更新冰箱条目
@fridge.route('/api/fridge/<int:item_id>', methods=['PUT'])
def update_fridge_item(item_id):
    item = Fridge.query.get(item_id)
    if not item:
        return jsonify({'error': 'Fridge item not found'}), 404
    data = request.json
    item.type = data.get('type', item.type)
    item.name = data.get('name', item.name)
    item.quantity = data.get('quantity', item.quantity)
    item.currency = data.get('currency', item.currency)
    item.price = data.get('price', item.price)
    item.expiry_days = data.get('expiry_days', item.expiry_days)
    item.expiry_date = data.get('expiry_date', item.expiry_date)
    item.photo = data.get('photo', item.photo)
    item.user_id = data.get('user_id', item.user_id)
    db.session.commit()
    return jsonify({'message': f'Fridge item updated successfully for id {item_id}'})

# 删除冰箱条目
@fridge.route('/api/fridge/<int:item_id>', methods=['DELETE'])
def delete_fridge_item(item_id):
    item = Fridge.query.get(item_id)
    if not item:
        return jsonify({'error': 'Fridge item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Fridge item deleted successfully for id {item_id}'})
