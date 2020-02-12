import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, Comment, tostring
from UIrecorder import Models as mdls
import re


def open_file_records(file_name: str) -> Element:
    tree = ET.parse(file_name)
    return tree.getroot()


def get_events(xml_el: Element):
    return xml_el.findall('Event')


def get_event_type(el: Element) -> mdls.EventType:
    ty = el.find('ev_type')
    if ty.text == 'EventType.MOUSE_CLICK':
        return mdls.EventType.MOUSE_CLICK
    if ty.text == 'EventType.MOUSE_UP':
        return mdls.EventType.MOUSE_UP
    if ty.text == 'EventType.MOUSE_MOVE':
        return mdls.EventType.MOUSE_MOVE
    if ty.text == 'EventType.KEYB_PRESS':
        return mdls.EventType.KEYB_PRESS
    if ty.text == 'EventType.KEYB_RELEASE':
        return mdls.EventType.KEYB_RELEASE
    if ty.text == 'EventType.SCROLL_UP':
        return mdls.EventType.SCROLL_UP
    if ty.text == 'EventType.SCROLL_DOWN':
        return mdls.EventType.SCROLL_DOWN


def get_position(el: Element) -> (float, float):
    pos = el.find('position')
    pos_str = str(pos.text)
    xy = re.findall('\d+', pos_str)
    return float(str(xy[0])), float(str(xy[1]))


def get_key(el: Element) -> str:
    key = el.find('key')
    return key.text


def get_time(el: Element) -> float:
    ti = el.find('time')
    return ti.text


def get_list_events(xml_el: Element) -> [mdls.EventRecorded]:
    event_list = [mdls.EventRecorded]
    evnts = get_events(xml_el)
    for e in evnts:
        _type = get_event_type(e)
        _pos = get_position(e)
        _key = get_key(e)
        _time = get_time(e)
        event_list.append(mdls.EventRecorded(_type, _pos, _key, _time))
        print(str(_type) + ' ' + str(_pos) + ' '+_key + ' ' + str(_time))

    return event_list
