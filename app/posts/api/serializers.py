from flask_restful import fields

creator_serilizer ={
    "id": fields.Integer,
    "name": fields.String
}

posts_serializers = {
    "id": fields.Integer,
    "name":fields.String,
    "image":fields.String,
    "description":fields.String,
    "creator_id":fields.Integer,
    "creator" :fields.Nested(creator_serilizer),
}
