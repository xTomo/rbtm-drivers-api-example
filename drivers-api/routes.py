from flask import Blueprint, request
import json
from . import hardware_mock as hw


bp_main = Blueprint('main', __name__, url_prefix='/')

bp_motor = Blueprint('motor', __name__, url_prefix='/motor/<int:motor_id>')


# Base route
@bp_main.route('/', methods=['GET'])
def main_route():
    return 'rbtm-drivers API example'


# Motor routes
@bp_motor.after_request
def after_request(response):
    header = response.headers
    header['Content-Type'] = 'application/json; charset=utf-8'
    return response


@bp_motor.route('/', methods=['GET'])
def get_state(motor_id):

    motor_state, error = hw.get_motor_state(motor_id)
    success = error is None

    return create_response(
        success=success,
        result=motor_state,
        error=error
    )


@bp_motor.route('/', methods=['POST'])
def set_state(motor_id):

    json_data, error = check_request(request.data)
    success = error is None

    if not success:
        return create_response(
            success=success,
            error=error
        )

    motor_state, error = hw.set_motor_state(motor_id, json_data)

    return create_response(
        success=error is None,
        result=motor_state,
        error=error
    )


# functions
def create_response(success=True, error=None, result=None):
    response_dict = {
        'success': success,
        'error': error,
        'result': result,
    }
    return json.dumps(response_dict)


def check_request(request_data):

    if not request_data:
        return None, create_response(success=False, error='Request is empty')

    try:
        request_data_dict = json.loads(request_data)
    except TypeError:
        return None, create_response(success=False, error='Request has not JSON data')
    else:
        return request_data_dict, None
