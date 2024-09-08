from flask import Blueprint

creator_blueprint = Blueprint('creators', __name__, url_prefix='/creators')
from app.creators import views