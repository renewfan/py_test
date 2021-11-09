from flask import Flask
from models import db
from User.views import user
from Content.views import content
from untils.filters import number_split

app = Flask(__name__, static_folder='assets')
# 使用配置
app.config.from_object('config.DevConfig')

# db与flask绑定
db.init_app(app)

# 入口文件中注册蓝图
# 注册用户蓝图
app.register_blueprint(user,url_prefix='/user')
# 注册内容蓝图
app.register_blueprint(content,url_prefix='/')
# 注册过滤函数
app.jinja_env.filters['number_split'] = number_split