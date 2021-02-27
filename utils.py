# [Project NLUS]
# 0.1.0va, 21.02.27. First launched.
# written by sjoon-oh
# 
# Legal stuff:
#   This simple code follows MIT license. 
# 
# MIT License
# Copyright (c) 2021 sjoon-oh
# 
# sjoon.oh.dev@pm.me
import re

def text_with_newlines(elem):
    text = ''
    for e in elem.descendants:
        if isinstance(e, str): text += e.strip()
        elif e.name == 'p' or e.name == 'br': text += '<br>'

    text = re.sub('<br><br>(<br>)+', '<br><br>', text)
    return text