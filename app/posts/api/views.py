from flask_restful import Resource, Api, marshal_with
from app.models import  db, Post
from app.posts.api.serializers import  posts_serializers
from app.posts.api.parsers import  post_parser

class PostsList(Resource):
    @marshal_with(posts_serializers)
    def get(self):
        posts=  Post.query.all()
        return posts

    @marshal_with(posts_serializers)
    def post(self):
        post_args = post_parser.parse_args() 
        new_post = Post(**post_args)
        db.session.add(new_post)
        db.session.commit()
        return new_post

class PostResource(Resource):
    @marshal_with(posts_serializers)
    def get(self,id):
        post = Post.query.get_or_404(id)
        return post

    @marshal_with(posts_serializers)
    def put(self,id):
        post = Post.query.get_or_404(id)
        post_args = post_parser.parse_args()
        post.name = post_args['name']
        post.description = post_args['description']
        post.image = post_args['image']
        db.session.commit() 
        return post
     

    def delete(self,id):
        post = Post.query.get_or_404(id)
        db.session.delete(post)  
        db.session.commit() 
        return {"message": "Post deleted successfully"}