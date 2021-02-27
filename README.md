# NLUS3
Successor of project nyscec3.

Project NLUS3 is the web-scraping project for LUS site, the online-learning site for Yonsei University students.

This has been updated from NYSCEC3, and shares quite-alike code base. This was due to the updated UI of the original YSCEC site, and some errors found from NYSCEC3.

General refactoring has been done, and there are some additional updates in logging in to the site. The project runs on the Github Action, so it does not need any standalone server.

## Setup
### Github Action
General setup for Github Action follows the same with the predecessor NYSCEC3. The link is given below:

[https://github.com/sjoon-oh/nyscec3](https://github.com/sjoon-oh/nyscec3)

Please follow the instruction in the link above for Github Action setting only.

*The Github Action setting file is named as python-package.yml in this repo.*


### Filling in Your Information

Be sure to fork/upload this repository to your Github account as a private repo. Sensitive information should be provided to the project to run without errors.

Please fill in your information in config.py. The personal information should be:

- Your LUS account
- Your SMTP information (In this project, Gmail was set as default)


```python
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
```

Provide the email address to receive updates. The variable NLUS_SEND_TO is located under mail.py.

```python3
NLUS_SEND_TO = ''

def send_updated_notice(updated_notice):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[NLUS2] Notice Updates'
    msg['From'] = ''
```

## Caution

Before running, the database file (even dummy) should be located under db/. The files are:

- notice.json
- instance.json

Blank array are written as defaults.

And, manage the running interval for Github Action if you are free account.