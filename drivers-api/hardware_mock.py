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
