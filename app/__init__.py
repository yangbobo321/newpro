from flask import Flask
from config import config
from extensions import bootstrap, db, moment, mail

def create_app(config_name=None):
    if config_name is None:
        config_name = 'development'

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    from blueprints import blog_blue, admin_blue, auth_blue
    app.register_blueprint(blog_blue)
    app.register_blueprint(admin_blue)
    app.register_blueprint(auth_blue)
    return app


app = create_app('development')
