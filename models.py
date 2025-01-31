from pydantic import BaseModel, EmailStr, Field


class NewUserTemplateContext(BaseModel):
    """ The values which will be used to generate the html body from new user template. """

    first_name: str = Field(
        (...),
        title='First name of the user who we will send an email to',
        max_length=80,
        example='Bartholomew'
    )


class NewUserInput(BaseModel):
    """ These values must be sent to new user notification endpoint. """

    recipient: EmailStr
    context: NewUserTemplateContext


class ResetPasswordTemplateContext(BaseModel):
    """ The values to be used to generate the html body from password reset template. """

    uid: str = Field(
        (...),
        title='urlsafe_base64_encode of the user id in bytes',
        max_length=20,
        example='MyT'
    )
    token: str = Field(
        (...),
        title='default_token_generator.make_token for user',
        max_length=50,
        example='cgcnha-535d6ca5aba5679f273a9cbb87319b2d'
    )


class ResetPasswordInput(BaseModel):
    """ These values must be sent to reset password notification endpoint. """

    recipient: EmailStr
    context: ResetPasswordTemplateContext


class MailOutput(BaseModel):
    """ Just simple JSON resp from our endpoints """

    message: str
