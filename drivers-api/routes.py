from flask import Blueprint

bp_main = Blueprint('main', __name__, url_prefix='/')


# Base route
@bp_main.route('/', methods=['GET'])
def main_route():
    return 'rbtm-drivers API example'
