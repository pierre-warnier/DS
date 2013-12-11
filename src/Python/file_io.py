"""
All I/O except relp reading.
"""

import re
import itertools
import glob
import sys
import os

import config

RE_TOKENS = re.compile('\((.*?)\)')
def read_lemma(res=None, file_list=set()):
    """Read lemma from file described in config.py"""
    if not res: res = dict()
    cpt = 1
    for f in glob.glob(config.RELP_FILES):
        if f in file_list:
            print >> sys.stderr, 'LEMMA (%d): File already read: %s' % (cpt, f) 
            continue
        print >> sys.stderr, 'LEMMA (%d): Starting file: %s' % (cpt, f) 
        cpt += 1
        ok_words = False
        ok_lemma = False
        for line in open(f):
            line = line.strip()
            if line == 'Words':
                ok_words = True
            elif ok_words:
                words = RE_TOKENS.findall(line)
                ok_words = False
            if line == 'Lemma':
                ok_lemma = True
            elif ok_lemma:
                lemma = RE_TOKENS.findall(line)
                res.update(dict((i.lower(), j.lower())
                                 for i,j in itertools.izip(words, lemma)))
                ok_lemma = False
    return res

def read_stop_words():
    try:
        return set(stop_word.strip() for stop_word in open(config.STOP_WORDS))
    except:
        return set()

def read_en2us():
    return dict(line.lower().strip().split('\t') for line in open(config.EN2US))

def mk_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)

if __name__ == '__main__':
    pass
