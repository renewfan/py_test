from flask import Blueprint, render_template, flash, redirect, url_for

from User.form import RegisterForm
from User.form import LoginForm

from models import User, db, UserProfile

# 实例化一个用户蓝图对象
user = Blueprint('user', __name__, template_folder='templates', static_folder='../assets')

# 注册
@user.route('/register' ,methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    # 获取数据
    if register_form.validate_on_submit():
        username = register_form.user_name.data
        nickname = register_form.nick_name.data
        password = register_form.password.data
        try:
            use_obj = User(username=username, nickname=nickname, password=password)
            db.session.add(use_obj)
            user_profile = UserProfile(username=username, user=use_obj)
            db.session.add(user_profile)
            db.session.commit()
            flash('注册成功', 'success')
            return redirect(url_for('user.login'))
        except Exception as e:
            print(e)
            flash('注册失败', 'danger')
    return render_template('register.html', form=register_form)

# 登录
@user.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

# 个人中心
@user.route('/mine')
def mine():
    return render_template('mine.html')