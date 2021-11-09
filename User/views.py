from flask import Blueprint, render_template

# 实例化一个用户蓝图对象
user = Blueprint('user', __name__, template_folder='templates', static_folder='../assets')

# 注册
@user.route('/register')
def register():
    return render_template('register.html')

# 登录
@user.route('/login')
def login():
    return render_template('login.html')

# 个人中心
@user.route('/mine')
def mine():
    return render_template('mine.html')