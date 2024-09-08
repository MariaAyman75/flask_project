from flask_restful import reqparse


Creator_parser = reqparse.RequestParser()

Creator_parser.add_argument("name", required=True, type=str, help="Name is required")
