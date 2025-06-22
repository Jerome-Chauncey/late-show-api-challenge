from config import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    number = db.Column(db.String)

    appearances = db.relationship(
        'Appearance',
        back_populates = 'episode',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    
    
    
    serialize_rules = ('-appearances.episode',)