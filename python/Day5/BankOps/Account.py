ops={}
def create_account(name, balance=0):
    ops[name]=balance
    print("Account for", name, "created with balance", balance)

def deposite(account, amount):
    if account in ops:
        ops[account]+=amount
        print(amount, "deposited in", account,"'s account. New balance :", ops[account])
    else:
        print("Account not found")

def withdraw(account, amount):
    if account in ops:
        ops[account]-=amount
        print(amount, "withdrew from", account,"'s account. New balance :", ops[account])
    else:
        print("Account not found")

def checkbalance(account):
    if account in ops:
        print(account,"'s account balance is:", ops[account])
    else:
        print("Account not found")

def transfer_money(sender, receiver, amount):
    if sender in ops and receiver in ops:
        if ops[sender]>=amount:
            ops[sender]-=amount
            ops[receiver]+=amount
            print(amount, "Transferred from", sender, "to", receiver, "'s account")
        else:
            print("Insufficient Funds")
    else:
        print("One or both accounts not found")

create_account("Aman", 10000)
create_account("Arnav", 15000)
deposite("Aman", 5000)
withdraw("Arya", 5000)
withdraw("Arnav", 5000)
checkbalance("Arnav")
transfer_money("Aman", "Arnav", 3000)
checkbalance("Aman")
checkbalance("Arnav")