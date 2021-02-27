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

import config as cf
import json

import os.path

def compare_update_notice(notice_list):
    print('\nrunning compare_update_notice')

    if not os.path.isfile('%s/notice.json' % cf.NLUS_DB_DIR):
        with open('%s/notice.json' % cf.NLUS_DB_DIR, 'w') as db:
            db.write('[]')

    updated_list = []
    with open('%s/notice.json' % cf.NLUS_DB_DIR, 'r') as db:
        old_list = json.load(db)

    for notice in notice_list:
        if notice not in old_list:
            updated_list.append(notice)
            old_list.append(notice)
    
    with open('%s/notice.json' % cf.NLUS_DB_DIR, 'w') as db:
        db.write(json.dumps(old_list, indent=4))

    print('done compare_update_notice')
    return updated_list



def compare_update_instance(instance_list):
    print('\nrunning compare_update_instance')

    if not os.path.isfile('%s/instance.json' % cf.NLUS_DB_DIR):
        with open('%s/instance.json' % cf.NLUS_DB_DIR, 'w') as db:
            db.write('[]')

    updated_list = []
    with open('%s/instance.json' % cf.NLUS_DB_DIR, 'r') as db:
        old_list = json.load(db)

    for instance in instance_list:
        if instance not in old_list:
            updated_list.append(instance)
            old_list.append(instance)

    with open('%s/instance.json' % cf.NLUS_DB_DIR, 'w') as db:
        db.write(json.dumps(old_list, indent=4))

    print('done compare_update_instance')
    return updated_list

