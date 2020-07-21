from fanshim import FanShim


fanshim = FanShim()


def get_fan():
    state = fanshim.get_fan()

    if state == 1:
        response = "enabled"
    else:
        response = "disabled"

    response_object = {
        "status": response
    }

    return response_object, 200



def set_fan(status):
    if status == "enabled":
        state = True
    else:
        state = False

    fanshim.set_fan(state)

    response_object = {
        "status": status
    }

    return response_object, 200
