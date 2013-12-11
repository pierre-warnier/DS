"""
All that is language related.
"""

import re

import file_io

#####
# LEMMA: see main.py (hack)
#####
LEMMA = dict()

#TERMS = file_io.read_terms_heads()
STOP_WORDS = file_io.read_stop_words()

EN2US = file_io.read_en2us()

# results are src, dest
RE_HYPHEN = re.compile('^([^\d]+)-([^\d]+)$')
def hyphenisation(word):
    """Removes hyphens from a term."""
    return word.replace('-','') if RE_HYPHEN.match(word) else word

RE_NUMBER = re.compile('(:?[-<>+]?[,\.\d]+)%?[-:/]?(:?[,\.\d]+)?%?')
def number(word):
    """Groups numbers."""
    #if RE_NUMBER.match(word):
    #    print word,  RE_NUMBER.sub('#NUMBER#', word)
    return RE_NUMBER.sub('#number#', word)

RE_POSSESSIVE = re.compile("^(.*)'s$")
def possessive(word):
    """Removes trailing 's"""
    match = RE_POSSESSIVE.match(word)
    return match.group(1) if match else word

def quote(word):
    """Removes ' from the beginning or the end of a term."""
    return word.strip("'").strip('"')

def lemmatization(word):
    """Lemmatize a word."""
    return LEMMA.get(word, word)

def lower(word):
    """Lower the case of a word."""
    return word.lower()

def en2us(word):
    return EN2US.get(word, word)

RE_NONWORD = re.compile('''[\[\](){}'"`|<>]''')
def sstrip(word):
    return RE_NONWORD.sub('', word)

if __name__ == "__main__":
    pass
