import random

from sqlalchemy.exc import IntegrityError

from models import Admin, Category, Post, Comment
from extensions import db
from app import app
from faker import Faker
app_context = app.app_context()
app_context.push()

# 生成虚拟管理员
def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='Bluelog',
        blog_sub_title="No, I'm the real thing",
        name='mima kriyang',
        about='um,i, mimayang, had a fun time as member'
    )
    admin.set_password('helloflask')
    db.session.add(admin)
    db.session.commit()

fake = Faker()

# 生成虚拟分类
def fake_categories(count=10):
    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

# 生成虚拟文章
def fake_posts(count=50):
    for i in range(count):
        post = Post(
        title=fake.sentence(),
        body=fake.text(2000),
        category=Category.query.get(random.randint(1, Category.query.count())),
        timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()

# 生成虚拟评论
def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count * 0.1)
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        comment = Comment(
            author='mima krei',
            email='mima@qq.com',
            site='example.com',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()
    # 回复
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count())),
        )
        db.session.add(comment)
    db.session.commit()

