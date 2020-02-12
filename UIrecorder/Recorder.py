from pynput import mouse
from pynput import keyboard
from UIrecorder import TimerClass as timer
from UIrecorder import Models as mdl
from UIrecorder import FileRecorder as file_rec

t = timer.Timer()
RECORDING = False
EventList = list()
file_name_output = './records/albert.xml'


def on_press(key):
    try:
        ev = mdl.EventRecorded(mdl.EventType.KEYB_PRESS,
                               (0.0, 0.0),
                               format(key.char).strip('key.').strip("'"),
                               t.get_current_time())
        ev.set_dict()
        EventList.append(ev)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    global RECORDING
    ev = mdl.EventRecorded(mdl.EventType.KEYB_RELEASE, (0.0, 0.0),
                           format(key).strip('key.').strip("'"), t.get_current_time())
    ev.set_dict()
    EventList.append(ev)
    if key == keyboard.Key.esc:
        stop_recorder()
        return False


def on_scroll(x, y, dx, dy):
    if dy < 0:
        ev = mdl.EventRecorded(mdl.EventType.SCROLL_DOWN, (x, y), 'scr_down', t.get_current_time())

    else:
        ev = mdl.EventRecorded(mdl.EventType.SCROLL_UP, (x, y), 'scr_up', t.get_current_time())
    ev.set_dict()
    EventList.append(ev)


def on_move(x, y):
    if len(EventList) == 0:
        return
    ev = mdl.EventRecorded(mdl.EventType.MOUSE_MOVE, (x, y), 'mse_mv', t.get_current_time())
    ev.set_dict()
    last: mdl.EventRecorded = EventList[-1]
    print(last.ev_type)
    if str(last.ev_type).__eq__(str(mdl.EventType.MOUSE_MOVE)):
        # print('modificate last move')
        last.position = (x, y)
    else:
        print('create new move')
        EventList.append(ev)


def on_click(x, y, button, pressed):
    if pressed:
        ev = mdl.EventRecorded(mdl.EventType.MOUSE_CLICK, (x, y), button, t.get_current_time())
    else:
        ev = mdl.EventRecorded(mdl.EventType.MOUSE_UP, (x, y), button, t.get_current_time())
    ev.set_dict()
    EventList.append(ev)


def start_recording():
    global RECORDING
    if not RECORDING:
        RECORDING = True
        t.start()
        listenerKb.start()
        print('KeyBoard listener started')
        listener.start()
        print('Mouse listener started')
        print('start Recording')
        while RECORDING:
            pass


def stop_recorder():
    global RECORDING
    if RECORDING:
        print('Stoping record')
        listener.stop()
        listenerKb.stop()
        t.stop()
        records = file_rec.make_xml(EventList)
        file_rec.save_record(file_name_output, records)
        RECORDING = False


listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)


listenerKb = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
