from flask import Blueprint
import json
from . import hardware_mock as hw


bp_main = Blueprint('main', __name__, url_prefix='/')

bp_motor = Blueprint('motor', __name__, url_prefix='/motor/<int:motor_id>')


# Base route
@bp_main.route('/', methods=['GET'])
def main_route():
    return 'rbtm-drivers API example'


# Motor routes
@bp_motor.route('/', methods=['GET'])
def get_state(motor_id):

    motor_state, error_message = hw.get_motor_state(motor_id)
    success = True if error_message is None else False

    return create_response(
        success=success,
        result=motor_state,
        error_message=error_message
    )


# functions
def create_response(success=True, error_message=None, result=None):
    response_dict = {
        'success': success,
        'error': error_message,
        'result': result,
    }
    return json.dumps(response_dict)
