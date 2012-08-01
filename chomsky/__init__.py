"""
Welcome.  Welcome to chomsky.
"""
from .buffer import *
from .exceptions import *
from .matchers import *
from .grammar import *
from .result import *


# aliases
A = Letter
L = Literal
W = Chars  # short for 'Word', for compatibility with pyparse
S = Whitespace  # short for 'Space'
R = Regex


# hide some Matchers
del AutoSequence
del AutoAny
del to_matcher
