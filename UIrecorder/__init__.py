from enum import Enum
from os import path
from UIrecorder import Player as player
from UIrecorder import Recorder as recorder
import argparse


class ActionType(Enum):
    PLAY = 0
    RECORD = 1


def get_parser():
    parser = argparse.ArgumentParser(description='RECORD and PLAY actions under Windows environment')
    parser.add_argument('Action', type=str, choices=['PLAY', 'RECORD'],
                        help='Play recorded actions with RECORD option or create Record with RECORD arg')
    parser.add_argument('File', default='./records/default.xml', type=str,
                        help='xml file path to work')
    return parser


if __name__ == '__main__':
    p = get_parser().parse_args()
    if p.Action.__eq__(str(ActionType.PLAY.name)):
        print('Performing ' + str(ActionType.PLAY.name) + ' of file ' + p.File)
        if path.isfile(p.File):
            player.init(p.File)
            player.play()
        else:
            print(p.File + " -> file doesn't exist!")
    if p.Action.__eq__(str(ActionType.RECORD.name)):
        recorder.file_name_output = p.File
        print('Performing ' + str(ActionType.RECORD.name) + ' in file ' + p.File)
        recorder.start_recording()

