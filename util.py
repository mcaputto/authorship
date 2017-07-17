'''Helper functions.'''

from glob import iglob
from os import path
from re import sub
from sys import maxunicode
from unicodedata import category


def _max(d):
    '''Return dictionary key with the maximum value.'''
    return max(d, key=d.get)


def _percent(d):
    '''Convert dictionary values to percentage.'''
    total = sum(d.values())
    for k in d:
        d[k] /= total
    return None


def _get_features(filename, translator):
    '''Return list of features.'''
    f = open(filename, 'r')
    text = f.read()
    f.close()
    # Make lowercase based on Unicode Standard 3.13
    text = text.lower()
    # Remove stopchars
    text.translate(translator)
    # Separate into list by whitespace
    text_list = text.split()
    return text_list


def _get_words(filename):
    '''Return list of words from a filename.'''
    with open(filename, 'r') as f:
        return f.read().split()


def _name(filename):
    '''Return filename without leading path and extension.'''
    if filename[-4:] == '.txt':
        return sub(r'.*/', '', filename[:-4])
    else:
        return sub(r'.*/', '', filename)


def _remove_unicode(begin_char):
    '''Create a dictionary with Unicode characters mapped to None.'''
    condition = 'category(chr(key)).startswith(begin_char)'
    return {key: None for key in range(maxunicode) if condition}


def _yield_name(directory, extension):
    '''Yield filenames contained in a directory.'''
    return iglob(path.join(directory, extension))
