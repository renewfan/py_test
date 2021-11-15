from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class RegisterForm(FlaskForm):
    # 注册
    user_name = StringField(label='用户名', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'
    })
    nick_name = StringField(label='昵称', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入昵称'
    })
    password = PasswordField(label='密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    })
    confirm_password = PasswordField(label='确认密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入确认密码'
    })


class LoginForm(FlaskForm):
    # 登录
    user_name = StringField(label='用户名', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'
    })
    password = PasswordField(label='密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    })
