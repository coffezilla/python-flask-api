
from flask import Blueprint

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def posts():
    return "Posts"
