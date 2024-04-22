from flask import Flask
from config import Config
from dashboard.index import index
from db import db
from route.dish_details_routes import dish_details
from route.dish_square_route import dish_square
from route.fridge_route import fridge
from route.ingredients_lsit_route import ingredients_list
from route.shopping_cart_route import shopping_cart
from route.user_info_route import user_info


def create_app():
    # 创建 Flask 程序
    app = Flask(__name__)
    # 导入配置
    app.config.from_object(Config)
    # 初始化app
    db.init_app(app)

    # 注册菜品详情相关蓝图
    app.register_blueprint(dish_details)
    # 注册菜品详情相关蓝图
    app.register_blueprint(dish_square)
    # 注册冰箱相关蓝图
    app.register_blueprint(fridge)
    # 注册材料清单相关蓝图
    app.register_blueprint(ingredients_list)
    # 注册购物车相关蓝图
    app.register_blueprint(shopping_cart)
    # 注册用户信息相关蓝图
    app.register_blueprint(user_info)

    # 前端视图
    # index主页面
    app.register_blueprint(index)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
