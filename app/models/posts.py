from . import db
from ..schemas.post_schema import PostSchema


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Post {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
