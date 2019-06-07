from flask import Blueprint, request
import json
from . import hardware_mock as hw


bp_main = Blueprint('main', __name__, url_prefix='/')

bp_source = Blueprint('source', __name__, url_prefix='/source')
bp_shutter = Blueprint('shutter', __name__, url_prefix='/shutter')
bp_motor = Blueprint('motor', __name__, url_prefix='/motor/<int:motor_id>')


# Base route
@bp_main.route('/', methods=['GET'])
def main_route():
    return json.dumps({'success': True, 'description': 'rbtm-drivers API example'})


# Source routes
@bp_source.route('/', methods=['GET'])
def get_source_state():

    source_state, error = hw.get_source_state()
    success = error is None

    return create_response(
        success=success,
        result=source_state,
        error=error
    )


@bp_source.route('/', methods=['POST'])
def set_source_state():

    json_data, error = check_request(request.data)
    success = error is None

    if not success:
        return create_response(
            success=success,
            error=error
        )

    source_state, error = hw.set_source_state(json_data)

    return create_response(
        success=error is None,
        result=source_state,
        error=error
    )


# Shutter routes
@bp_shutter.route('/', methods=['GET'])
def get_shutter_state():

    shutter_state, error = hw.get_shutter_state()
    success = error is None

    return create_response(
        success=success,
        result=shutter_state,
        error=error
    )


@bp_shutter.route('/', methods=['POST'])
def set_shutter_state():

    json_data, error = check_request(request.data)
    success = error is None

    if not success:
        return create_response(
            success=success,
            error=error
        )

    shutter_state, error = hw.set_shutter_state(json_data)

    return create_response(
        success=error is None,
        result=shutter_state,
        error=error
    )


# Motor routes
@bp_motor.route('/', methods=['GET'])
def get_motor_state(motor_id):

    motor_state, error = hw.get_motor_state(motor_id)
    success = error is None

    return create_response(
        success=success,
        result=motor_state,
        error=error
    )


@bp_motor.route('/', methods=['POST'])
def set_motor_state(motor_id):

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
