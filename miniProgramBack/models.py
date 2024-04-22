from db import db

# 定义数据库模型类
class UserInfo(db.Model):
    # 定义用户信息表模型...
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    recipe_count = db.Column(db.Integer, default=0)
    like_count = db.Column(db.Integer, default=0)
    photo = db.Column(db.String(255))

    def __repr__(self):
        return f'UserInfo(id={self.id}, name={self.name}, recipe_count={self.recipe_count}, like_count={self.like_count})'


class DishDetails(db.Model):
    # 定义菜谱详情表模型...
    __tablename__ = 'dish_details'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    recipe = db.Column(db.Text)
    method = db.Column(db.Text)
    photo = db.Column(db.String(255))
    user_id_author = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    user_id_like = db.Column(db.String(255))

    # 定义关系属性
    author = db.relationship('UserInfo', backref='dishes', foreign_keys=[user_id_author])

    def __repr__(self):
        return f'DishDetails(id={self.id}, name={self.name}, user_id_author={self.user_id_author}, user_id_like={self.user_id_like})'


class DishSquare(db.Model):
    # 定义菜品广场表模型...
    __tablename__ = 'dish_square'

    id=db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    hotness = db.Column(db.Integer)

    def __repr__(self):
            return f'DishSquare(id={self.id}, dish_id={self.dish_id}, author_id={self.author_id}, hotness={self.hotness})'



class Fridge(db.Model):
    # 定义冰箱表模型...
    __tablename__ = 'fridge'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    currency = db.Column(db.String(10))
    price = db.Column(db.Numeric(10, 2))
    expiry_days = db.Column(db.Integer)
    expiry_date = db.Column(db.Date)
    photo = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    user = db.relationship('UserInfo', backref='fridges')

    def __repr__(self):
        return f'Fridge(id={self.id}, name={self.name}, user_id={self.user_id}, quantity={self.quantity})'

class IngredientsList(db.Model):
    # 定义材料清单表模型...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish_details.id'), nullable=False)

    def __repr__(self):
        return f'IngredientsList(id={self.id}, name={self.name}, quantity={self.quantity}, dish_id={self.dish_id})'



class ShoppingCart(db.Model):
    # 定义购物车表模型...
    __tablename__ = 'shopping_cart'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    name = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(50))
    quantity = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    user = db.relationship('UserInfo', backref='shopping_carts')

    def __repr__(self):
        return f'ShoppingCart(id={self.id}, name={self.name}, user_id={self.user_id}, quantity={self.quantity})'