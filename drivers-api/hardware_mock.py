import time


def get_source_state():

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    state = 'I am an X-ray source'
    result = {'state': state}

    return result, None


def set_source_state(new_state):

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    value = new_state['switch']

    state = 'X-ray source state is {} now'.format(value)
    result = {'state': state}

    return result, None


def get_shutter_state():

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    state = 'I am a shutter'
    result = {'state': state}

    return result, None


def set_shutter_state(new_state):

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    value = new_state['switch']

    state = 'Shutter state is {} now'.format(value)
    result = {'state': state}

    return result, None


def get_motor_state(motor_id):

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

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


def set_motor_state(motor_id, new_state):

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

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


def get_detector_state():

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    state = 'I am a Detector'
    result = {'state': state}

    return result, None


def set_detector_state(new_state):

    # time.sleep is used to emulate devices respond lag
    time.sleep(1)

    state = 'Detector state is updated to {}'.format(new_state)
    result = {'state': state}

    return result, None
