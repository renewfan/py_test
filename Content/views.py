from flask import Blueprint, render_template, request, abort

# 实例化一个用户蓝图对象
from models import Question

content = Blueprint('content', __name__, template_folder='templates', static_folder='../assets')

# 首页
@content.route('/')
def index():
    return render_template('index.html')

# 关注
@content.route('/follow')
def follow():
    limit = 20
    page = int(request.args.get('page', 1))
    # 获取数据
    q_data = Question.query.filter_by(is_valid=True).paginate(page=page, per_page=limit)
    return render_template('follow.html', q_data=q_data)

# 问答
@content.route('/write')
def write():
    return render_template('write.html')

# 详情
@content.route('/detail/<int:id>')
def detail(id):
    # 问题详情数据
    data = Question.query.get(id)
    if not data.is_valid:
        abort('404')
    # 详情的第一条回答
    answer_data = data.answer_list.filter_by(is_valid=True).first()
    return render_template('detail.html', data=data, answer_data=answer_data)