#######################################################################
#   1. რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)
#######################################################################

def greet_recursively(times):
    if times > 0:
        print(f"Hello!")
        greet_recursively(times - 1,)

# ფუნქციის გამოძახება
greet_recursively(13)



#######################################################################
#2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.
#######################################################################


def process_order(item, quantity=None):
    try:
        # შეცდომის შემოწმება
        if quantity is not None and quantity < 0:
            raise ValueError("რაოდენობა უნდა იყოს 0-ზე მეტი")

        # რაოდენობის დაბეჭდვა
        if quantity is not None:
            print(f"კერძი: {item}, რაოდენობა: {quantity}")
        else:
            quantity = 1
            print(f"კერძი: {item}, რაოდენობა: {quantity}")

    except ValueError as e:
        # შეცდომის დაბეჭდვა
        print(f"შეცდომა: {e}")
        quantity = 1
        print(f"შეკვეთა: {item}, რაოდენობა: {quantity}")

# ფუნქციის გამოძახება
process_order("კერძი1", 15)
process_order("კერძი2")


#######################################################################
# 3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს.
#######################################################################

def calculate_product(a, b, c):
    result = a * b * c
    return result

# 3 რიცხვების შემოტანა
num1 = float(input("შემოიტანე პირველი რიცხვი: "))
num2 = float(input("შემოიტანე მეორე რიცხვი: "))
num3 = float(input("შემოიტანე მესამე რიცხვი: "))

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
result = calculate_product(num1, num2, num3)
print(f"ნარმავლი: {result}")