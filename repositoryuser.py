#! /usr/bin/env python3
# repositoryuser.py

from models import UserModel
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def create_user(self, signup: UserModel) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True

    def get_user(self):
        return self.sess.query(UserModel).all()

    def get_user_by_username(self, username: str):
        return self.sess.query(UserModel).filter(UserModel.username == username).first()