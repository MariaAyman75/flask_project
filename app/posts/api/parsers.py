from flask_restful import reqparse


post_parser = reqparse.RequestParser()

post_parser.add_argument("name", required=True, type=str, help="Name is required")
post_parser.add_argument("image", required=True, type=str, help="Image is required")
post_parser.add_argument("description", required=True, type=str, help="Description is required")
post_parser.add_argument("creator_id", required=True, type=int, help="Creator ID is required")