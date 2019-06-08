import time


def sleep(seconds):
    def sleep_decorator(func):
        def wrapper(*args, **kwargs):

            # time.sleep is used to emulate devices respond lag
            time.sleep(seconds)

            return func(*args, **kwargs)
        return wrapper
    return sleep_decorator


@sleep(1)
def get_source_state():

    state = 'I am an X-ray source'
    result = {'state': state}

    return result, None


@sleep(1)
def set_source_state(new_state):

    value = new_state['switch']

    state = 'X-ray source state is {} now'.format(value)
    result = {'state': state}

    return result, None


@sleep(1)
def get_shutter_state():

    state = 'I am a shutter'
    result = {'state': state}

    return result, None


@sleep(1)
def set_shutter_state(new_state):

    value = new_state['switch']

    state = 'Shutter state is {} now'.format(value)
    result = {'state': state}

    return result, None


@sleep(1)
def get_motor_state(motor_id):

    state = None

    if motor_id == 0:
        state = 'I am a vertical motor'
    elif motor_id == 1:
        state = 'I am a horizontal motor'
    elif motor_id == 2:
        state = 'I am an angle motor'

    error_message = None if state else 'There is no motor with id {}'.format(motor_id)
    result = {'motor_id': motor_id, 'state': state} if state else None

    return result, error_message


@sleep(5)
def set_motor_state(motor_id, new_state):

    state = None

    if motor_id == 0:
        state = 'Vertical motor state is updated to {}'.format(new_state)
    elif motor_id == 1:
        state = 'Horizontal motor state is updated to {}'.format(new_state)
    elif motor_id == 2:
        state = 'Angular motor state is updated to {}'.format(new_state)

    error_message = None if state else 'There is no motor with id {}'.format(motor_id)
    result = {'motor_id': motor_id, 'state': state} if state else None

    return result, error_message


@sleep(1)
def get_detector_state():

    state = 'I am a Detector'
    result = {'state': state}

    return result, None


@sleep(1)
def set_detector_state(new_state):

    state = 'Detector state is updated to {}'.format(new_state)
    result = {'state': state}

    return result, None
