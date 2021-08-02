from app import db
from flask import render_template, request, url_for, current_app
from app.models import econ_fulltext
from app.main import bp


@bp.route('/')
@bp.route('/home')
def index():
    return render_template("home.html", title='Home')


@bp.route('/articles', methods=['GET'])
def articles():
    page = request.args.get('page', 1, type=int)
    articles = econ_fulltext.query.order_by(econ_fulltext.id).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('home', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('home', page=articles.prev_num) \
        if articles.has_prev else None
    return render_template('home.html', articles=articles, 
                           next_url=next_url, prev_url=prev_url)
    
@bp.route('/test', methods=['GET'])
def test():
    articles = econ_fulltext.query.order_by(econ_fulltext.id).all()
    return render_template('home.html', articles=articles)