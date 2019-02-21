# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    new_string = []
    for i in list(s):
        new_string.append(i * 2)
    return ''.join(new_string)
