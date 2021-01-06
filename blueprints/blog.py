from blueprints import blog_blue
from flask import render_template, request, current_app
from models import Post
from app import db


@blog_blue.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    pagination = Post.query.order_by(Post.id.asc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('index.html', pagination=pagination, posts=posts)


@blog_blue.route('/about')
def about():
    return render_template('about.html')


@blog_blue.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('category.html', category_id=category_id)


@blog_blue.route('/post/<int:post_id>')
def show_post(post_id):
    return render_template('post.html')

# 创建数据表
@blog_blue.route('/create_table')
def create_table():
    try:
        db.drop_all()
        db.create_all()
        tips = '成功了'
    except:
        tips = '出错啦'

    return tips
