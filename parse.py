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

import requests
from bs4 import BeautifulSoup # parser
import json

# 
# user defined
import config as cf
import utils

#
# Parses the main notice board (Comprehensive)
def parse_notice(session):
    print('\nrunning parse_notice')
    notice_list = []

    print('getting to %s' % cf.NLUS_BOARD_NOTICE)
    res = session.get(cf.NLUS_BOARD_NOTICE)
    print('done. status code: %s' % (res.status_code))
    
    soup = BeautifulSoup(
        str(BeautifulSoup(res.text, 'html.parser').find("tbody")),
        'html.parser')

    for notice in soup.findAll('a'):
        notice_list.append({'title': " ".join(notice.text.split()), 'href': notice.attrs['href']})

    for notice in notice_list:
        content = BeautifulSoup(session.get(notice['href']).text, 'html.parser').find('div', class_='text_to_html')
        notice['content'] = utils.text_with_newlines(content)

        print('- %s, %s' % (notice['title'], notice['href'])) # For debug purpose

    print('done parse_notice')
    return notice_list


#
# Parsing entry
def parse_instance(session):
    print('\nrunning parse_instance')
    entry_list = []
    instance_list = []

    print('getting to %s' % cf.NLUS_BASE)
    res = session.get(cf.NLUS_BASE)
    print('done. status code: %s' % (res.status_code))

    # First parse entry
    for entry in BeautifulSoup(
        str(BeautifulSoup(res.text, 'html.parser').find(
            'ul', class_='my-course-lists coursemos-layout-0')), 'html.parser'
        ).findAll('a'):
        
        entry_list.append({'title': BeautifulSoup(str(entry), 'html.parser').find('h3').text, 'href': entry.attrs['href']})

    for entry in entry_list:
        print(entry['title'])
        instances = BeautifulSoup(session.get(entry['href']).text, 'html.parser').findAll('span', class_='instancename')
        entry['instances'] = []

        for instance in instances:
            instance_list.append({'entry': entry['title'], 'instance': instance.text})
            print('- %s' % instance.text)

    print('done parse_instance')
    return instance_list

#
# Parsing entry
def parse_qna(session):
    print('\nrunning parse_qna') 
    qna_list = []

    print('maybe later!')

    print('done parse_instance')
    return qna_list

