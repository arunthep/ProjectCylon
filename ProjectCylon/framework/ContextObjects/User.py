# -*- coding: utf-8 -*-

class User:
    UserName = None
    Password = None
    AdminAccess = False
    def __init__(self,
                 UserName = "DefaultUserName",
                 Password = "DefaultPassword", ):
        self.UserName = UserName
        self.Password = Password

