from flask import Flask
from app.config import config_options  
from app.models import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api
from flask_login import LoginManager
# from flask_wtf import CSRFProtect

login_manager = LoginManager()
# csrf = CSRFProtect()

def create_app(config_name='prd'):

    app = Flask(__name__)

    current_config = config_options[config_name]  
    app.config.from_object(current_config)  
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
  
    db.init_app(app)
    migrate = Migrate(app, db)

    bootstrap = Bootstrap5(app)
    api = Api(app)

    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    # csrf.init_app(app)

    from app.posts import post_blueprint
    app.register_blueprint(post_blueprint)
    
    from app.creators import creator_blueprint
    app.register_blueprint(creator_blueprint)

    from app.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)


    from app.posts.api.views import  PostsList,PostResource
    api.add_resource(PostsList, '/api/posts')
    api.add_resource(PostResource, '/api/posts/<int:id>')

    from app.creators.api.views import  CreatorsList,CreatorResource
    api.add_resource(CreatorsList, '/api/creators')
    api.add_resource(CreatorResource, '/api/creators/<int:id>')


    return app


@login_manager.user_loader
def load_user(user_id):
    from app.models import Creator
    return Creator.query.get(int(user_id))