from app import db
client_rieltor_table=db.Table(
    'client_rieltor',
     db.Column('client_id',db.Integer,db.ForeignKey('clients.id'),primary_key=True),
     db.Column('rieltor_id',db.Integer,db.ForeignKey('rieltors.id'),primary_key=True)
)