from flask import Blueprint, jsonify, request
from db import db
from models import DishSquare, DishDetails, UserInfo

## 创建名为 'index' 的用户相关蓝图
index = Blueprint('index', __name__)

@index.route('/api/index', methods=['GET'])
def get_dish_square():
    # 查询 dish_square 表，并将相关信息合并后按热度排序返回
    dish_squares = DishSquare.query.order_by(DishSquare.hotness.desc()).all()
    dish_square_details = []
    for dish_square in dish_squares:
        dish_detail = DishDetails.query.get(dish_square.dish_id)
        user = UserInfo.query.get(dish_square.author_id)

        dish_square_details.append({
            'id': dish_square.id,
            'dish_name': dish_detail.name,
            'dish_photo': dish_detail.photo,
            'dish_like_count':dish_detail.user_id_like.count(',')+1,
            'author_name': user.name,
            'author_photo': user.photo,
            'hotness': dish_square.hotness
        })

    return jsonify({'dish_square_details': dish_square_details})