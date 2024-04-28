from logo import project_logo
from new_user import Create_Account
from old_user import Old_User
from account_lists import Old_Accounts
from random import randint
import os
import pickle
print(project_logo)


print("WELCOME TO OUR BANK......!")
print("How can i help you ? (Type : new_account / existed_account )")
choice = input()
if choice == "new_account":
    print("Creating a new account...........")
    input_name = input("Name: ")
    input_DOB = input("Date of Birth: ")
    input_aadhar = input("Aadhar No.: ")
    input_PAN = input("PAN No.: ")
    input_mobile = input("Mobile No.: ")

    # Generating account number to the new user......
    account = []
    for i in range(0, 12):
        account.append(str(randint(0, 9)))
    account_number = ' '.join(account)
    # Setting password.......
    print("Create a strong password (atleast 6 characters): ")
    password = input()

    print("Thank you for creating new account in our bank, Would you like to deposit or fixed deposit ?")

    choice_deposit = input()
    if choice_deposit == "deposit":
        amount = int(input("How much money you would like to deposit... "))
        Create_Account.deposit(amount)
        Create_Account(input_name, input_DOB, input_aadhar, input_PAN, input_mobile,amount,account_number,password)
        my_account = {input_name: {"account_number": account_number, "password": password, "balance": amount,
                         "mobile_no": input_mobile, "DOB": input_DOB, "Aadhar": input_aadhar}}
    elif choice_deposit == "fixed_deposit":
        amount_fd = int(input("How much money you would like to fixed deposit...  "))
        Create_Account.fixed_deposit(amount_fd)
        Create_Account(input_name, input_DOB, input_aadhar, input_PAN, input_mobile,amount_fd,account_number,password)
        my_account = {input_name: {"account_number": account_number, "password": password, "balance": amount_fd,
                         "mobile_no": input_mobile, "DOB": input_DOB, "Aadhar": input_aadhar}}
    # appending the new account to old account lists......
    with open("EXISTED_ACCOUNTS.txt",mode = 'w') as EA:
        EA.write(str(Old_Accounts))
        EA.close()



elif choice == "existed_account":
    #SECURITY CHECK..........................

    def Security(name, ac_number, password):
        global flag
        for key in Old_Accounts.keys():
            if key != name:
                continue

            else:
                if Old_Accounts[name]["account_number"] == ac_number:
                    if Old_Accounts[name]["password"] == password:
                        print("Your access granted... ")
                        flag = 1
                    else:
                        print("Your password is INVALID")
                else:
                    print("Your Login Credentials are INVALID, Please try again.... ")


    print("Enter the Login Credentials.........")
    flag = 0
    while True:
        if flag == 1:
            break
        input_name = input("Username: ")
        input_account_number = input("Account No.: ")
        input_password = input("Password: ")
        Security(input_name,input_account_number,input_password)

    print("Would you like to check your account details: Type( yes / no)")
    choice_details = input().lower()
    if choice_details == "yes":
        Old_User.details(input_name)
    elif choice_details == "no":
        print("Would you like to withdrawl or deposit to your account ? Type( withdrawl/deposit)")
        decision = input().lower()
        if decision == "withdrawl":
            input_withdrawl = int(input("Enter the amount: "))
            Old_User.withdrawl(input_name,input_withdrawl)
        elif decision == "deposit":
            input_deposit = int(input("Enter the amount: "))
            Old_User.new_deposit(input_deposit)










