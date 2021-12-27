from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    cors = CORS(app, resources={r'/*': {"origins": '*'}})
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app