from . import db
class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    in_url=db.Column(db.String(4000))
    out_url=db.Column(db.String(4000))
    

    