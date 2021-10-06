#!/usr/bin/python3
"""
    prints a text
"""


def text_indentation(text):
    """
        prints a text
    """
    flag = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        text = text.replace('.', '.\n\n')
        text = text.replace('?', '?\n\n').replace(':', ':\n\n')
        textL = text.split('\n\n')
        last = len(textL)
        for i in textL:
            flag += 1
            a = i.lstrip()
            if flag < last:
                print(a + '\n')
            else:
                print(a, end="")
