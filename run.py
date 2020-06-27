#!/usr/bin/env python3.8
from user import User

def create_user(name, password):
    new_user = User(name, password)
    return new_user

def save_user(user):
    user.save_user()

def del_user(user):
    user.delete_user()


