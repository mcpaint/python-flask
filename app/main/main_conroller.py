from flask import Blueprint, render_template

api = Blueprint('main', __name__, url_prefix='/')


@api.route('/')
def index():
    title = 'Index Page..'
    return render_template('main/index.html', title=title)
