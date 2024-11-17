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
