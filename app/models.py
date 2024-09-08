from flask_sqlalchemy import  SQLAlchemy
from flask import  url_for
from flask_login import UserMixin

db= SQLAlchemy()
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('creators.id'), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for('static', filename=f"blog/images/{self.image}")

    @property
    def show_url(self):
        return url_for('posts.details', post_id=self.id)

    @property
    def delete_url(self):
        return url_for('posts.delete', post_id=self.id)
    
    @property
    def edit_url(self):
        return url_for('posts.edit', post=self.id)


class Creator(db.Model, UserMixin):
    __tablename__ = 'creators'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    posts = db.relationship('Post', backref='creator')

# class Creator(db.Model):
#     __tablename__ = 'creators'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     posts= db.relationship('Post', backref='creator')
    
    def __str__(self):
        return self.name

    @property
    def show_url(self):
        return url_for('creators.details', id=self.id)

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)