from app import db
from app.search import query_index

class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total


class econ_fulltext(SearchableMixin, db.Model):
    __searchable__ = ['text']
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), unique=False)
    text = db.Column(db.Text, unique=False)
    
    def __repr__(self):
        return '<title {}>'.format(self.title)