from flask import Flask, jsonify, request
from config import Config
from db import db
from models import DishDetails

def create_app():
    # 创建 Flask 程序
    app = Flask(__name__)
    # 导入配置
    app.config.from_object(Config)
    # 初始化app
    db.init_app(app)

    # 添加路由和请求处理逻辑...
    @app.route('/api/dish_details', methods=['GET'])
    def get_dish_details():
        # 处理 GET 请求，返回菜品详情数据
        dish_details = DishDetails.query.all()
        dish_details_json = []
        for dish in dish_details:
            dish_details_json.append({
                'id': dish.id,
                'name': dish.name,
                'recipe': dish.recipe,
                'method': dish.method,
                'photo': dish.photo,
                'user_id_author': dish.user_id_author,
                'user_id_like': dish.user_id_like
            })
        return jsonify({'dish_details': dish_details_json})

    @app.route('/api/dish_details', methods=['POST'])
    def add_dish_details():
        # 处理 POST 请求，添加菜品详情数据
        data = request.json
        new_dish_details = DishDetails(
            name=data['name'],
            recipe=data['recipe'],
            method=data['method'],
            photo=data['photo'],
            user_id_author=data['user_id_author'],
            user_id_like=data['user_id_like']
        )
        db.session.add(new_dish_details)
        db.session.commit()
        return jsonify({'message': 'Dish details added successfully'})

    @app.route('/api/dish_details/<int:dish_id>', methods=['PUT'])
    def update_dish_details(dish_id):
        # 处理 PUT 请求，更新菜品详情数据
        data = request.json
        dish_details = DishDetails.query.get(dish_id)
        if not dish_details:
            return jsonify({'error': 'Dish details not found'}), 404
        dish_details.name = data.get('name', dish_details.name)
        dish_details.recipe = data.get('recipe', dish_details.recipe)
        dish_details.method = data.get('method', dish_details.method)
        dish_details.photo = data.get('photo', dish_details.photo)
        dish_details.user_id_author = data.get('user_id_author', dish_details.user_id_author)
        dish_details.user_id_like = data.get('user_id_like', dish_details.user_id_like)
        db.session.commit()
        return jsonify({'message': f'Dish details updated successfully for dish {dish_id}'})

    @app.route('/api/dish_details/<int:dish_id>', methods=['DELETE'])
    def delete_dish_details(dish_id):
        # 处理 DELETE 请求，删除菜品详情数据
        dish_details = DishDetails.query.get(dish_id)
        if not dish_details:
            return jsonify({'error': 'Dish details not found'}), 404
        db.session.delete(dish_details)
        db.session.commit()
        return jsonify({'message': f'Dish details deleted successfully for dish {dish_id}'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
