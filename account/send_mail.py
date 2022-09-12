import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from typing import List
from dotenv import load_dotenv
load_dotenv('.env')

conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_FROM = os.getenv('MAIL_FROM'),
    MAIL_PORT = int(os.getenv('MAIL_PORT')),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='account/templates/'
)

async def send_email(email: EmailStr, code: str):
    context = {
        "email_text_detail": """
                        Thanks for creating account.
                        Please verify your account
                            """,
        "email": email,
        "activation_code": List[code]
    }
    message = MessageSchema(
        subject='Activation code',
        recipients=List[email],
        body=str(context), 
        subtype = 'html'
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')

