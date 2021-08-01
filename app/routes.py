from app import db, app
from flask import render_template, request, url_for
from models import Econ_fulltext


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():

    full_text = Econ_fulltext.query.all()
    page = request.args.get('page', 1, type=int)
    
    texts=full_text.text.order_by(Econ_fulltext.id).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('home', page=texts.next_num) \
        if texts.has_next else None
    prev_url = url_for('home', page=texts.prev_num) \
        if texts.has_prev else None
    
    return render_template("home.html", title='Home', )
