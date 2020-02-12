from pysxm import ComplexType
from dicttoxml import dicttoxml
import xml.dom.minidom as dom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, Comment, tostring


class Event(ComplexType):
    sequence = ('ev_type', 'position', 'key', 'time')

    def __init__(self, event: dict):
        self.ev_type = event['ev_type']
        self.position = event['position']
        self.key = event['key']
        self.time = event['time']


def get_xml(dictionary):
    return dicttoxml(dictionary, custom_root='Event', attr_type=False)


def make_xml(events: list) -> Element:
    root = ET.Element('EventsRecorded')
    root.set('version', '1.0')
    comment = Comment('Generated with UIrecorder ABGSoftDevelop')
    root.append(comment)

    for evnt in events:
        d: dict = evnt.my_dict
        if d is None:
            continue
        xml = get_xml(d)
        xml_el = get_element(xml.decode())
        root.append(xml_el)

    print(prettify(root))
    return root


def get_element(el_str: str) -> ET.ElementTree:
    return ET.fromstring(el_str)


def prettify(elem):
    rough_string = tostring(elem, 'utf-8')
    reparsed = dom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def save_record(file_name: str, root: Element):
    tree = ET.ElementTree(root)
    tree.write(file_name.replace('.xml', '') + '.xml')
