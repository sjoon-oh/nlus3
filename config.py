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

NLUS_LOGIN_PARAM = {
    'username': '',
    'password': ''
    }

NLUS_SMTP_LOGIN = {
    'id': '',
    'pw': ''
}

NLUS_SMTP_SERVER = 'smtp.gmail.com'
NLUS_SMTP_PORT = 465

NLUS_BASE = 'https://open.yonsei.ac.kr'
NLUS_INFRA_BASE = 'https://infra.yonsei.ac.kr/'

NLUS_LOGIN_INDEX = '%s/login.php' % NLUS_BASE
NLUS_LOGIN_COURSEMOSLOGIN = '%s/passni/sso/coursemosLogin.php' % NLUS_BASE

NLUS_LOGIN_PMSSOSERVICE = '%s/sso/PmSSOService' % NLUS_INFRA_BASE
NLUS_LOGIN_PMSSOAUTHSERVICE = '%s/sso/PmSSOAuthService' % NLUS_INFRA_BASE

NLUS_LOGIN_SPLOGINDATA = '%s/passni/sso/spLoginData.php' % NLUS_BASE
NLUS_LOGIN_SPLOGINPROCESS = '%s/passni/spLoginProcess.php' % NLUS_BASE

NLUS_BOARD_NOTICE = '%s/mod/ubboard/my.php' % NLUS_BASE

# for import from parent directory
import sys, os
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# stores payload templates
NLUS_TEMPLATE_DIR = './payloads_template'
NLUS_DB_DIR = './db'

NLUS_INFO = \
"""
Project NLUS: Renewed parser for former nyscec.
0.1.0va, 21.02.27. First launched, written by SukJoon Oh
https://github.com/sjoon-oh/, contact me sjoon.oh.dev@pm.me
"""