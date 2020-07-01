#!/usr/bin/env python3.8
from user import User
from user import Credentials

def create_user(name, password):
    new_user = User(name, password)
    return new_user

def save_user(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def create_account(account, username, passwrd):
    new_account = Credentials(account,username,passwrd)
    return new_account

def save_account(Credentials):
    Credentials.save_account()

def delete_account(Credentials):
    Credentials.delete_account()

def show_account(Credentials):
    return Credentials.show_accounts()

#def generate_password(credentials):
    
def search_accounts(cls, search):
    return Credentials.search_accounts(search)











def main():
    print("Hello, Welcome to password Locker")
    print('\n')
    print('a - create an account  b - exit')
    choice = input()
    if choice == 'a':
        print("enter your name")
        name = input()         
        print("enter a password")
        password = input()         
        save_user(create_user(name, password))
        print("-"*10)
        print(f'{name}, confirm password')
        success = input()
        if success == password:
            print('login successful')
            while True:
                print("-"*10)
                print("use these short codes for your functions today: nu - new user, ex - exit the user, aa = add an account, gp - generate password for a new account, da - display all saved accounts, sa - search for accounts, da - delete account ")
                short_code = input().lower()
                #log on to an existing account
                if short_code == 'aa':
                    print("enter the existing account eg instagram")
                    print("account name")
                    account = input()
                    print('login name')
                    username = input()
                    print('passwords')
                    passwrd = input()
                    save_account(create_account(account, username,passwrd))
                    print('\n')
                    print(f'You have successfully logged in')
                #new user new account 
                elif short_code == 'nu':
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
                #display all accounts
                elif short_code == 'da':
                    if show_account() != []:
                        print('A list of all your accounts')
                # search accounts
                elif short_code ==  'sa':
                    print('What would you like to search for?')
                    search = input()
                    if search_accounts(search):
                        found = search_accounts(search)
                        print('here is what we found:')
                        print(found.account + found.username + found.passwrd)
                # delete account 
                elif short_code == 'da' :
                    print('what account would you like to delete?')
                    acc = input()
                    if search_accounts(acc):
                        delete_account(search_accounts(acc))
                        print('account deleted successfully ')
                #exit account
                elif short_code == 'ex':
                    print(f'exist successful, {name}')
                    break
                else: 
                    print("Invalid, try again!")


if __name__ == '__main__':

    main()
