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

import json
import config as cf

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

NLUS_SEND_TO = ''


def send_updated_notice(updated_notice):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[NLUS2] Notice Updates'
    msg['From'] = ''
    msg['To'] = NLUS_SEND_TO

    text_frame_upper = """<p>Hi there,
    there are some new updates from NLUS2.</p><br>
    """
    text_frame_lower="""<p>
    From NLUS.<br><br>
    You are receiving this letter due to a subscription.<br>
    Send your information to <b>sjoon.oh.dev@pm.me</b> to unsubscribe.<br>
    https://github.com/sjoon-oh
    </p>
    """
    text = ''
    
    for notice in updated_notice:
        text += '<b>%s : </b><br>' % notice['title']
        text += '%s<br><br>' % notice['content']

    msg.attach(MIMEText('Notice Updates', 'plain'))
    msg.attach(MIMEText(
        text_frame_upper + 
        text +
        text_frame_lower,
        'html'))

    smtp_server = smtplib.SMTP_SSL(cf.NLUS_SMTP_SERVER, cf.NLUS_SMTP_PORT)
    smtp_server.login(cf.NLUS_SMTP_LOGIN['id'], cf.NLUS_SMTP_LOGIN['pw'])

    smtp_server.sendmail(msg['From'], msg["To"], msg.as_string())


def send_updated_instance(updated_instance):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[NLUS2] Instance Updates'
    msg['From'] = ''
    msg['To'] = NLUS_SEND_TO

    text_frame_upper = """<p>Hi there,
    there are some new updates from NLUS2.</p><br>
    """
    text_frame_lower="""<p>
    From NLUS.<br><br>
    You are receiving this letter due to a subscription.<br>
    Send your information to <b>sjoon.oh.dev@pm.me</b> to unsubscribe.<br>
    https://github.com/sjoon-oh
    </p>
    """
    text = ''

    for instance in updated_instance:
        text += '<b>%s</b> : ' % instance['entry']
        text += '%s<br>' % instance['instance']

    msg.attach(MIMEText('Instance Updates', 'plain'))
    msg.attach(MIMEText(
        text_frame_upper + 
        text +
        text_frame_lower,
        'html'))

    smtp_server = smtplib.SMTP_SSL(cf.NLUS_SMTP_SERVER, cf.NLUS_SMTP_PORT)
    smtp_server.login(cf.NLUS_SMTP_LOGIN['id'], cf.NLUS_SMTP_LOGIN['pw'])

    smtp_server.sendmail(msg['From'], msg["To"], msg.as_string())