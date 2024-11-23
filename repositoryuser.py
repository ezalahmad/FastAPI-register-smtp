#! /usr/bin/env python3
# repositoryuser.py

# from sqlalchemy.orm import Session
# from models import UserModel
# from sqlalchemy.orm import Session
#
# import smtplib
# from email.message import EmailMessage
#
# class UserRepository:
#     def __init__(self, sess: Session):
#         self.sess: Session = sess
#
#     def create_user(self, signup: UserModel) -> bool:
#         try:
#             self.sess.add(signup)
#             self.sess.commit()
#         except:
#             return False
#         return True
#
#     def get_user(self):
#         return self.sess.query(UserModel).all()
#
#     def get_user_by_username(self, username: str):
#         return self.sess.query(UserModel).filter(UserModel.username == username).first()
#
# class SendEmailVerify:
#
#     def sendVerify(token):
#         email_address = "ezalahmad@gmail.com" # fastapi-login
#         email_password = "jzqb elzo afak ydar"
#
#         # msg = EmailMessage()
#         # msg["Subject"] = "Email Verification"


# from sqlalchemy.orm import Session
# from models import UserModel
# from sqlalchemy.orm import Session
#
# import smtplib
# from email.message import EmailMessage

from sqlalchemy.orm import Session
from models import UserModel
from typing import Dict,Any
from sqlalchemy.orm import Session

import smtplib
from email.message import EmailMessage

class UserRepository:
    def __init__(self,sess:Session):
        self.sess: Session=sess

    def create_user(self,signup:UserModel) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True

    def get_user(self):
        return  self.sess.query(UserModel).all()

    def get_user_by_username(self,username:str):
        return self.sess.query(UserModel).filter(UserModel.username==username).first()

    # def update_user(self,id:int,details:Dict[str,Any]) -> bool:
    #     try:
    #         self.sess.query(UserModel).filter(UserModel.id==id).update(details)
    #         self.sess.commit()
    #     except:
    #         return False
    #     return True
    # def delete_user(self,id:int)-> bool:
    #     try:
    #         self.sess.query(UserModel).filter(UserModel.id==id).delete()
    #         self.sess.commit()
    #     except:
    #         return  False
    #     return  True

class SendEmailVerify:

    def sendVerify(token):
        email_address = "smtp_admin@pythonhat.com" # fastapi-login
        # email_password = "h3ll0_br0ther"

        # read password from file
        with open('password.txt') as f:
            email_password = f.read().strip()

        # create email
        msg = EmailMessage()
        msg['Subject'] = "Email subject"
        msg['From'] = email_address
        msg['To'] = "ezalahmad@gmail.com" # type Email
        msg.set_content(
                f"""\
                        verify account
        http://localhost:8000/user/verify/{token}
        """,

        )
        # send email
        with smtplib.SMTP_SSL('mail.pythonhat.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)


# class SendEmailVerify:
#     def sendVerify(token):
#         email_address = "smtp_admin@pythonhat.com"
#
#         with open('password.txt') as f:
#             email_password = f.read().strip()
#
#         msg = EmailMessage()
#         msg['Subject'] = "Email subject"
#         msg['From'] = email_address
#         msg['To'] = "ezalahmad@gmail.com"
#         msg.set_content(f"verify account: http://localhost:8000/user/verify/{token}")
#
#         try:
#             with smtplib.SMTP_SSL('mail.pythonhat.com', 465) as smtp:
#                 smtp.login(email_address, email_password)
#                 smtp.send_message(msg)
#         except Exception as e:
#             print(f"Error sending email: {e}")
#             raise HTTPException(status_code=500, detail="Failed to send email.")

