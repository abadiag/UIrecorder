from enum import Enum


class EventType(Enum):
    KEYB_PRESS = 0
    KEYB_RELEASE = 1
    MOUSE_CLICK = 2
    MOUSE_UP = 3
    MOUSE_MOVE = 4
    SCROLL_DOWN = 5
    SCROLL_UP = 6


class EventRecorded:
    ev_type = ''
    position = ''
    key = ''
    time = ''
    my_dict = None

    def __init__(self, _type: EventType, pos: (float, float), _key: str, _time: float):
        self.ev_type = str(_type)
        self.position = str(pos)
        self.key = str(_key)
        self.time = str(_time)

    def set_dict(self):
        self.my_dict = {
            'ev_type': self.ev_type,
            'position': self.position,
            'key': self.key,
            'time': self.time
            }
