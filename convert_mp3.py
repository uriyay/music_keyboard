#!/usr/bin/python

import pydub
import sys

def convert(path, out_path=None):
    if not path.endswith('.mp3'):
        raise Exception('Its not mp3 file')

    if out_path is None:
        out_path = path.split('.mp3')[0] + '.wav'

    song = pydub.AudioSegment.from_mp3(path)
    song.export(out_path, format='wav')

if __name__ == '__main__':
    convert(*sys.argv[1:])
