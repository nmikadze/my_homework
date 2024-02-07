# აბანკო ანგარიშის კლასი, მომხმარებლის, პაროლის და საწყისი თანხის პარამეტრებით. თანხის შეტანის, გამოტანის და გადარიცხვის,   და დარჩენილი ნაშთის ჩვენების მეთოდებით. __repr__ მეჯიქ მეთოდით.
# პაროლის ცვლადი უნდა იყოს private _ ცვლადი და საჭიროა აკმაყოფილებდეს პირობას: მინიმალური სიმბოლოების ოდენობა _ 8
####################################################
class BankAccount:
    def __init__(self, username, password, initial_balance=0):
        self._password = password
        self.username = username
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        print(f"დეპოზიტზე შემოთანილია {amount} ლარი. მიმდინარე ბალანსი: {self._balance} ლარი.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"დეპოზიტიდან გატანილია {amount} ლარი. New მიმდინარე ბალანსი: {self._balance} ლარი.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"მიმდინარე ბალანსი: {self._balance} ლარი.")

    def __repr__(self):
        return f"BankAccount(username='{self.username}', balance={self._balance})"


# პროგრამის გამოყენება
def main():
    username = input("მომხმარებლის სახელი: ")
    password = input("შეიყვანე პაროლი (min 8 სიმბოლო): ")
    while len(password) < 8:
        print("პაროლი უნდა იყოს 8 სიმბოლოზე მეტი.")
        password = input("შეიყვანე პაროლი : ")

    initial_balance = float(input("შეიყვანე საწყისი ბალანსი: "))
    account = BankAccount(username, password, initial_balance)

    while True:
        print("\nაირჩიე ქმედენა:")
        print("1. დეპოზიტზე თანხის შეტანა")
        print("2. გატანა")
        print("3. ბალანსის შემოწმება")
        print("4. Exit")

        choice = input("აირჩიე სასურველი ქმედება: ")

        if choice == "1":
            amount = float(input("შეიყვანე დეპოზიტის თანხის ოდენობა: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("შეიყვანე დეპოზიტიდან თანხის გატანის ოდენობა: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("გამოსვლა.")
            break
        else:
            print("არასწორი არჩევანი. აირჩიე სწორი ოპერაცია .")


if __name__ == "__main__":
    main()

