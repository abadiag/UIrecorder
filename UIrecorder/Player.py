from UIrecorder import FileReader as f_reader
from UIrecorder import TimerClass as timer
import pyautogui as auto
from UIrecorder import Models as mdls


events_loaded = []
t = timer.Timer()


def init(file='./records/albert.xml'):
    global events_loaded
    records = f_reader.open_file_records(file)
    events_loaded = f_reader.get_list_events(records)
    print(auto.position())


def play():
    if len(events_loaded) > 0:
        t.start()
        start_play()


def stop():
    pass


def get_position(pos):
    pos = pos.strip('(').strip(')')
    x = pos.split(',')[0]
    y = pos.split(',')[1]
    x = float(x)
    y = float(y)
    return x, y


def get_button(button: str):
    return button.split('.')[1]


def perform_click(pos):
    position = get_position(pos)
    x = position[0]
    y = position[1]
    auto.click(x, y)


def perform_keypress(key: str):
    # auto.keyDown(key)
    auto.press(key)


def perform_key_release(key: str):
    auto.keyUp(key)


def perform_scroll(pos, _dspl):
    position = get_position(pos)
    x = position[0]
    y = position[1]
    perform_move(pos)
    auto.scroll(clicks=_dspl, x=x, y=y)


def perform_move(pos):
    position = get_position(pos)
    print('called position ' + str(position) + ' autogui pos ' + str(auto.position()))
    x = position[0]
    y = position[1]
    auto.moveTo(x=x, y=y)


def perform_mouse_down(pos, button):
    position = get_position(pos)
    x = position[0]
    y = position[1]
    auto.mouseDown(x=x, y=y, button=get_button(button))


def perform_mouse_up(pos, button):
    position = get_position(pos)
    x = position[0]
    y = position[1]
    auto.mouseUp(x=x, y=y, button=get_button(button))


def start_play():
    ev = events_loaded.pop(1)
    print('event loaded, next event at ' + str(ev.time))
    while len(events_loaded) > 1:
        if t.get_current_time() > float(ev.time):
            # print('performing event ' + str(ev.ev_type))
            if str(ev.ev_type).__eq__(str(mdls.EventType.MOUSE_CLICK)):
                perform_mouse_down(ev.position, ev.key)
            if str(ev.ev_type).__eq__(str(mdls.EventType.MOUSE_UP)):
                perform_mouse_up(ev.position, ev.key)
            if str(ev.ev_type).__eq__(str(mdls.EventType.KEYB_PRESS)):
                perform_keypress(ev.key)
            if str(ev.ev_type).__eq__(str(mdls.EventType.KEYB_RELEASE)):
                perform_key_release(ev.key)
            if str(ev.ev_type).__eq__(str(mdls.EventType.SCROLL_UP)):
                perform_scroll(ev.position, 100)
            if str(ev.ev_type).__eq__(str(mdls.EventType.SCROLL_DOWN)):
                perform_scroll(ev.position, -100)
            if str(ev.ev_type).__eq__(str(mdls.EventType.MOUSE_MOVE)):
                perform_move(ev.position)
                t.sleep(1)
            ev = events_loaded.pop(1)
