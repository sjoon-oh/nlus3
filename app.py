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
# import db

print(cf.NLUS_INFO)
print('starting sesstion')
with requests.Session() as s:

    #
    # Step 1. Generate cookie.
    print('getting to %s' % (cf.NLUS_LOGIN_INDEX))
    res = s.get(cf.NLUS_LOGIN_INDEX)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 2. Throw the user information
    with open('%s/login.json'%cf.NLUS_TEMPLATE_DIR, 'r') as template:
        payload = json.load(template)
        payload['username'] = cf.NLUS_LOGIN_PARAM['username']
        payload['password'] = cf.NLUS_LOGIN_PARAM['password']

    print('posting to %s with\n%s' % 
        (cf.NLUS_LOGIN_COURSEMOSLOGIN, json.dumps(payload, indent=3)))
    res = s.post(cf.NLUS_LOGIN_COURSEMOSLOGIN, payload)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 3. Throw again with S1 parameter
    with open('%s/PmSSOService.json'%cf.NLUS_TEMPLATE_DIR, 'r') as template:
        payload = json.load(template)
        payload['S1'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='S1').get('value'))
        payload['username'] = cf.NLUS_LOGIN_PARAM['username']
        payload['password'] = cf.NLUS_LOGIN_PARAM['password']

    print('posting to %s with\n%s' % 
        (cf.NLUS_LOGIN_PMSSOSERVICE, json.dumps(payload, indent=3)))
    res = s.post(cf.NLUS_LOGIN_PMSSOSERVICE, payload)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 4. Throw again with keyModulus parameters to coursemosLogin URI
    with open('%s/coursemosLogin.json'%cf.NLUS_TEMPLATE_DIR, 'r') as template:
        payload = json.load(template)
        payload['ssoChallenge'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='ssoChallenge').get('value'))
        payload['keyModulus'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='keyModulus').get('value'))
        payload['keyExponent'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='keyExponent').get('value'))
        payload['username'] = cf.NLUS_LOGIN_PARAM['username']
        payload['password'] = cf.NLUS_LOGIN_PARAM['password']

    print('posting to %s with\n%s' % 
        (cf.NLUS_LOGIN_COURSEMOSLOGIN, json.dumps(payload, indent=3)))
    res = s.post(cf.NLUS_LOGIN_COURSEMOSLOGIN, payload)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 5. Need to generate RSA Public Key
    # pip install pyjsbn-rsa
    # pip install six

    from jsbn import RSAKey

    rsa = RSAKey()
    rsa.setPublic(
        payload['keyModulus'],
        payload['keyExponent']
        )

    E2 = rsa.encrypt(json.dumps({
        'userid': payload['username'], 
        'userpw': payload['password'], 
        'ssoChallenge': payload['ssoChallenge']
    }))

    print('E2 encryption done: %s' % E2)
    
    #
    # Step 6. Toss again with E2 combined.
    with open('%s/PmSSOAuthService.json'%cf.NLUS_TEMPLATE_DIR, 'r') as template:
        payload = json.load(template)
        payload['S1'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='S1').get('value'))
        payload['E2'] = E2
        payload['username'] = cf.NLUS_LOGIN_PARAM['username']
        payload['password'] = cf.NLUS_LOGIN_PARAM['password']

    print('posting to %s with\n%s' % 
        (cf.NLUS_LOGIN_PMSSOAUTHSERVICE, json.dumps(payload, indent=3)))
    res = s.post(cf.NLUS_LOGIN_PMSSOAUTHSERVICE, payload)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 7. Toss again with E3, E4, E5, S2 attached
    with open('%s/spLoginData.json'%cf.NLUS_TEMPLATE_DIR, 'r') as template:
        payload = json.load(template)

        payload['E3'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='E3').get('value'))
        payload['E4'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='E4').get('value'))
        payload['S2'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='S2').get('value'))
        payload['CLTID'] = str(BeautifulSoup(res.text, 'html.parser').find(
            'input', id='CLTID').get('value'))
        payload['username'] = cf.NLUS_LOGIN_PARAM['username']
        payload['password'] = cf.NLUS_LOGIN_PARAM['password']

    print('posting to %s with\n%s' % 
        (cf.NLUS_LOGIN_SPLOGINDATA, json.dumps(payload, indent=3)))
    res = s.post(cf.NLUS_LOGIN_SPLOGINDATA, payload)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 8. Finalizing the login process
    print('getting to %s' % cf.NLUS_LOGIN_SPLOGINPROCESS)
    res = s.get(cf.NLUS_LOGIN_SPLOGINPROCESS)
    print('done. status code: %s' % (res.status_code))

    #
    # Step 9. Let's parse
    import parse as ps

    notice_list = ps.parse_notice(s)
    instance_list = ps.parse_instance(s)
    # qna_list = ps.parse_qna(s)

    #
    # Step 10. Compare!!
    import compare as cm

    updated_notice = cm.compare_update_notice(notice_list)

    print('notice updates: ')
    print(json.dumps(updated_notice, indent=3))

    updated_instance = cm.compare_update_instance(instance_list)

    print('entry updates: ')
    print(json.dumps(updated_instance, indent=3))

    
    #
    # Step 11. Send me noty
    import mail

    if len(updated_notice) != 0:
        mail.send_updated_notice(updated_notice)

    if len(updated_instance) != 0:
        mail.send_updated_instance(updated_instance)
