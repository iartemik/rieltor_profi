from .User import User
from .Client_Rieltor_Association import *
class Client(User):
    __tablename__='clients'
    rieltors=db.relationship('Rieltor',secondary=client_rieltor_table,backref='clients')
   


     
