from account_lists import Old_Accounts
class Old_User:

    def __init__(self,name,account_number,password):
        self.name = name
        self.account_number = account_number
        self.password = password

    def details(name):
        print(Old_Accounts[name])

    def withdrawl(input_name,withdrawl_money):
        print("Your balance before withdrawl :",Old_Accounts[input_name]["balance"])
        current_balance = Old_Accounts[input_name]["balance"] - withdrawl_money
        print(f"Your balance after withdrawl :{current_balance}")
        Old_Accounts[input_name]["balance"] = current_balance

    def new_deposit(self,deposit_money):
        print(f"Your balance before deposit : {Old_Accounts[input_name][balance]}")
        current_balance = Old_Accounts[input_name]["balance"] + deposit_money
        print(f"Your balance after deposit :{current_balance}")
        Old_Accounts[input_name]["balance"] = current_balance
