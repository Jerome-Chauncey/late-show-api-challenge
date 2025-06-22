from config import db, bcrypt
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)


# id

# username (unique)

# password_hash (hashed password)
