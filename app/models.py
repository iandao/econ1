from app import db

class Econ_fulltext(db.Model):
    __searchable__ = ['text']
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), unique=False)
    text = db.Column(db.Text, unique=False)
    
    def __repr__(self):
        return '<title {}>'.format(self.title)