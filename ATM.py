title = " Welcome to My ATM "
print(title.center(70, '#'))
def read_file():
    with open("credential.txt", 'r') as f:
     data = f.readlines()
 #   print(data[2])
    username = data[0].replace("\n", "")
    password = data[1].replace("\n", "")
    balance = int(data[2])
    return username, password, balance


def write_file(username,password,current_balance):
    with open("credential.txt", 'w') as f:
        f.writelines([username + '\n', password + '\n', str(current_balance)])


def Withdraw_Amount(current_balance):
    amount = int(input("Enter the amount to  be withdraw: "))
    current_balance = current_balance-amount
    write_file(username,password,current_balance)
    print(f"Transaction Complete. Your Available Balance: {current_balance}")
    print("Thank You !!!")
   # return current_balance


def Deposit_Amount(current_balance):
    amount = int(input("Enter the amount to  be deposit: "))
    current_balance = current_balance + amount
    write_file(username, password, current_balance)
    print(f"Transaction Complete. Your Available Balance: {current_balance}")
    print("Thank You! Visit Again!")
    #return current_balance


def change_password():
    current_password = input("Enter Your current password")
    if current_password == password :
        passcode = input(" Enter your new Password: ")
        write_file(username, passcode, current_balance)
        print(f"Password successfully changed. ")
        print("Thank You! Visit Again!")
     #   return passcode
    else:
        print("Invalid Password")
       # return password


name = input("Enter your username: ")

passcode = input("Enter your password: ")
username, password, current_balance = read_file()
if password != passcode:
    print("Invalid password")
else:
    print("1 : Withdraw Amount")
    print("2 : Deposit Amount")
    print("3 : Change Password")
    print("4 : Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      # balance= Withdraw_Amount(balance)
        Withdraw_Amount(current_balance)
      # print(f"Balance: {balance}")
    elif choice == '2':
       # balance = Deposit_Amount(balance)
        Deposit_Amount(current_balance)

    elif choice == '3':
        password = change_password()
        print(f"Your Password: {password}")
    else:
        print("Thank You! Visit Again!")
