from .User import User
from app import db


class Rieltor(User):
    __tablename__ = "rieltors"
    experience = db.Column(db.Integer)
    company = db.Column(db.String, nullable=True)
    info = db.Column(db.String)
