from flask_restful import Resource, Api, marshal_with
from app.models import  db, Creator
from app.creators.api.serializers import  creator_serilizer
from app.creators.api.parsers import  Creator_parser

class CreatorsList(Resource):
    @marshal_with(creator_serilizer)
    def get(self):
        creators=  Creator.query.all()
        return creators

    @marshal_with(creator_serilizer)
    def post(self):
        creator_args = Creator_parser.parse_args()  
        new_creator = Creator(**creator_args)
        db.session.add(new_creator)
        db.session.commit()
        return new_creator

class CreatorResource(Resource):
    @marshal_with(creator_serilizer)
    def get(self,id):
        creator = Creator.query.get_or_404(id)
        return creator

    @marshal_with(creator_serilizer)
    def put(self,id):
        creator = Creator.query.get_or_404(id)
        creator_args = Creator_parser.parse_args()
        creator.name = creator_args['name']
        db.session.commit() 
        return creator
     

    def delete(self,id):
        creator = Creator.query.get_or_404(id)
        db.session.delete(creator)  
        db.session.commit() 
        return {"message": "Creator deleted successfully"}