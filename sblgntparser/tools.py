import json
import os

import logging
log = logging.getLogger(__name__)

from pathlib import Path

def filelist(folderpath, ext=None, flat=True):
    '''
    Returns a list of all the files contained in the folder specified by `folderpath`.
    To filter the files by extension simply add a list containing all the extension with `.` as the second argument.
    If `flat` is False, then the Path objects are returned.
    '''
    path = Path(folderpath)
    if not ext:
        ext = []
    if path.exists() and path.is_dir():
        if flat:
            return [ str(f) for f in path.iterdir() if f.is_file() and f.suffix in ext ]
        else:
            return [ f for f in path.iterdir() if f.is_file() and f.suffix in ext ]
    else:
        log.warn('Nothing found in "{}"'.format(str(folderpath)))

def particles(category=None):
    '''
    Returns a dict containing old greek particles grouped by category.
    '''
    filepath = os.path.join(os.path.dirname(__file__), './particles.json')
    with open(filepath) as f:
        try:
            particles = json.load(f)
        except ValueError as e:
            log.error('Bad json format in "{}"'.format(filepath))
        else:
            if category:
                if category in particles:
                    return particles[category]
                else:
                    log.warn('Category "{}" not contained in particle dictionary!'.format(category))
            return particles

def bookname(bookindex):
    '''
    Returns the name of the book given the index.
    '''
    nt = {
        0: 'Matthew',
        1: 'Mark',
        2: 'Luke',
        3: 'John',
        4: 'Acts',
        5: 'Romans',
        6: 'Corinthians 1',
        7: 'Corinthians 2',
        8: 'Galatians',
        9: 'Ephesians',
        10: 'Philippians',
        11: 'Colossians',
        12: 'Thessalonians 1',
        13: 'Thessalonians 2',
        14: 'Timothy 1',
        15: 'Timothy 2',
        16: 'Titus',
        17: 'Philemon',
        18: 'Hebrews',
        19: 'James',
        20: 'Peter 1',
        21: 'Peter 2',
        22: 'John 1',
        23: 'John 2',
        24: 'John 3',
        25: 'Jude',
        26: 'Revelation'
    }
    # book indices are beginning from 1
    return nt[bookindex - 1]

def parts():
    '''
    Returns the dictionary with the part as key and the contained book as indices.
    '''
    parts = {
        'Canon': [ _ for _  in range(1, 5) ],
        'Apostle': [ 5 ],
        'Paul': [ _ for _ in range(6, 19) ],
        'General': [ _ for _ in range(19, 26) ],
        'Apocalypse': [ 27 ]
    }
    return parts