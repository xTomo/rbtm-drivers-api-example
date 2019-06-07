def get_motor_state(motor_id):

    state = motor_state(motor_id)
    error_message = None if state else 'There is no motor with id {}'.format(motor_id)
    result = {'motor_id': motor_id, 'state': state} if state else None

    return result, error_message


def motor_state(motor_id):

    if motor_id == 0:
        return 'I am a vertical motor'
    elif motor_id == 1:
        return 'I am a horizontal motor'
    elif motor_id == 2:
        return 'I am an angle motor'
    else:
        return None
