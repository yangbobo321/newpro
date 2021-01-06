from flask import Blueprint


blog_blue = Blueprint('blog', __name__)
admin_blue = Blueprint('admin', __name__, url_prefix='/admin')
auth_blue = Blueprint('auth', __name__, url_prefix='/auth')


from .blog import *
from .admin import *
from .auth import *
