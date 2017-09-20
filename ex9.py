"""Panagram A panagram is a sentence which contains all letters of the
alphabet.
Write a function called panagram which takes a string s as input. It
should return True if s is a panagram and False otherwise.
"""

import string
def panagram(s): # applicable only for lowercase letters
    az=string.ascii_lowercase 
    for i in az:
        if i not in s:
            return False
    return True
