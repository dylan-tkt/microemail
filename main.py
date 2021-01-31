from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from starlette.requests import Request

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

import logging
import os

from models import NewUserInput, ResetPasswordInput

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
templates = Jinja2Templates(directory='templates')

app = FastAPI()
logger = logging.getLogger('email')
conf = ConnectionConfig(
    MAIL_USERNAME = os.environ.get('SMTP_USERNAME'),
    MAIL_PASSWORD = os.environ.get('SMTP_PASSWORD'),
    MAIL_FROM = 'admin@wertkt.com',
    MAIL_PORT = os.environ.get('EMAIL_PORT', '2525'),
    MAIL_SERVER = os.environ.get('SMTP_SERVER'),
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)
fm = FastMail(conf)

FRONT_URL = 'http://example.com'


@app.post('/new-user/', response_model=NewUserInput)
async def new_user(data: NewUserInput):
    """ Send email welcoming a new user. """

    logger.info(f'new_user email input received: {data}')

    template = templates.get_template('new_user.html')
    body = template.render(data.context)
    restructured_data = {
        'recipients': [data.recipient],
        'subject': 'Thank you for your registration!',
        'body': body,
        'subtype': 'html',
    }
    message = MessageSchema(**restructured_data)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={'message': 'email has been sent'})


@app.post('/password-reset/', response_model=ResetPasswordInput)
async def password_reset(data: ResetPasswordInput):
    """ Send an email with a link to reset the user's password. """

    logger.info(f'password_reset input received: {data}')

    template = templates.get_template('password_reset.html')
    body = template.render(data.context, front_url=FRONT_URL)
    restructured_data = {
        'recipients': [data.recipient],
        'subject': 'Here is your password reset!',
        'body': body,
        'subtype': 'html',
    }
    message = MessageSchema(**restructured_data)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={'message': 'email has been sent'})
