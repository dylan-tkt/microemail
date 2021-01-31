from typing import List, Dict
from enum import Enum
from pydantic import BaseModel


class NewUserTemplateContext(BaseModel):
    """ The values which will be used to generate the html body from new user template. """

    first_name: str


class NewUserInput(BaseModel):
    """ These values must be sent to new user notification endpoint. """

    to_addr: str
    context: NewUserTemplateContext


class ResetPasswordTemplateContext(BaseModel):
    """ The values to be used to generate the html body from password reset template. """

    uid: str
    token: str


class ResetPasswordInput(BaseModel):
    """ These values must be sent to reset password notification endpoint. """

    to_addr: str
    context: ResetPasswordTemplateContext


class EmailReadyToSend(BaseModel):
    """ A prepared email that can be sent"""

    to_addrs: List[str]
    from_addr: str
    subject: str
    context: Dict[str, str]
    cc: List[str] = []
    bcc: List[str] = []
    attachments: List[bytes] = []