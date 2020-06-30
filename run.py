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
            print('\n')
            create_user_password= input()
            print("confirm")
            print('\n')
            confirm_password = input()
        else:
            print(f"account created successful {create_user_name}!")
            print("login")
            print('\n')
            typed_username = input()
            print("password")
            print('\n')
            typed_password = input()
        while typed_username != create_user_name or typed_password != create_user_password:
            print("invalid password or username, try again")
            print('\n')
            typed_username = input()
            print('\n')
            print("password")
            typed_password = input()
    elif short_code == 'lg':
        print("login")
        print('enter username')
        login_username = input()
        print('\n')
        print("password")
        login_userpassword = input()
        print('\n')
        while login_username != 'default' or login_userpassword != 'default-password':
            print ('invalid input for generic use user: default and password: 0000')
            print ('enter valid username')
            print('\n')
            login_username = input()
            print ('\n')
            login_userpassword = input()
        else:
            print('Your in')
    

        
            
        








if __name__ == '__main__':

    main()

            







