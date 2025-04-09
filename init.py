from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Base

db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
jwt = JWTManager()
bcrypt = Bcrypt()