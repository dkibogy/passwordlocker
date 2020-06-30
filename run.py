#!/usr/bin/env python3.8
from user import User

def create_user(name, password):
    new_user = User(name, password)
    return new_user

def save_user(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def main():
    print("Hello, Welcome to password Locker")
    print('\n')
    print("use these short codes: nu - new user,lg - login, ex - exit the user ")
    short_code = input().lower()
    if short_code == 'nu':
        print("create a new username")
        create_user_name= input()

        print("create a new password")
        create_user_password= input()

        print("confirm password")
        confirm_password = input()

        while confirm_password != create_user_password:
            print("wrong password")
            print("try again")
            create_user_password= input()
            print("confirm")
            confirm_password = input()
        else:
            print(f"account created successful {create_user_name}!")
            print("login")
            typed_username = input()
            print("password")
            typed_password = input()
        while typed_username != create_user_name or typed_password != create_user_password:
            print("invalid password or username, try again")
            typed_username = input()
            print("password")
            typed_password = input()
            


if __name__ == '__main__':

    main()

            







