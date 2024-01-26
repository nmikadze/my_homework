#   1.დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.
############################################################################################################
# საწყისი სია
numbers = [1, 2, 3, 4, 5]

# ყველა რიცხვს 2-ზე ვამრაბლებთ
result = list(map(lambda x: x * 2, numbers))

print(result)


############################################################################################################
#   2. დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)
############################################################################################################


 # საწყისი სია
name_list = ["John", "Alice", "Bob", "MAX", "emma"]

#
remove_small_names = lambda names: [name for name in names if name.isupper()]

# 
result = remove_small_names(name_list)

#print(result)

length = len(result)

print(length)

############################################################################################################
#   3. დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
############################################################################################################
# საწყისი სია
numbers = [1, -2, 3, -4, 5, -6]
#
positive_sum = sum(filter(lambda x: x > 0, numbers))
negative_sum = sum(filter(lambda x: x < 0, numbers))
#
print("Positive Sum:", positive_sum)
print("Negative Sum:", negative_sum)

############################################################################################################
# 4. დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
############################################################################################################



class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0 and less than or equal to the balance.")

# ექაუნთის შექმნა
account_holder_name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))

try:
    bank_account = BankAccount(account_holder_name, initial_balance)
    print("Bank account created successfully.")
except ValueError as e:
    print(f"Error creating bank account: {e}")

# Dდეპოზიტზე ოპერაციები
    
while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        try:
            deposit_amount = float(input("Enter deposit amount: "))
            bank_account.deposit(deposit_amount)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '2':
        try:
            withdraw_amount = float(input("Enter withdrawal amount: "))
            bank_account.withdraw(withdraw_amount)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
