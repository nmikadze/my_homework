import random

def generate_random_numbers_list(length, start_range, end_range):
    random_numbers = [random.randint(start_range, end_range) for _ in range(length)]
    return random_numbers

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
length = int(input("შემოიტანეთ სიას სიგრძე: "))
start_range = int(input("შემოიტანეთ სიას საწყისი მნიშვნელობა: "))
end_range = int(input("შემოიტანეთ სიას ბოლო მნიშვნელობა: "))

random_numbers_list = generate_random_numbers_list(length, start_range, end_range)
print("შემთხვევით მთელ რიცხვთა სია:", random_numbers_list)


# 2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.
sorted_list = sorted(random_numbers_list)

print ("შემთხვევით მთელ რიცხვთა სორტირებული სია: " , sorted_list)


# 3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.

# binary search

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid  # ინდექსი რომელზეც იმახსოვრებს ელემენტი
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # თუ ელემენტი არ მოიძებნა

# binary_search ფუნქციის გამოძახება
target_value = int(input("შემოიტანეთ საძებნი მნიშვნელობა: "))
target_index = binary_search(sorted_list, target_value)

if target_index != -1:
     print(f"{target_value} არსებობს სორტირებულ სიაში ინდექსით {target_index}.")
else:
    print(f"{target_value} არ არსებობს სორტირებულ სიაში!!!!!")



# linear_search
def linear_search(sorted_list, target):
    for i in range(len(sorted_list)):
        if sorted_list[i] == target:
            return i  # ინდექსი რომელზეც იმახსოვრებს ელემენტი
    return -1  # თუ ელემენტი არ მოიძებნა



# შესაძლო ელემენტი
target_value = int(input("შემოიტანეთ საძებნი მნიშვნელობა: "))

# linear_search ფუნქცია

target_index = linear_search(sorted_list, target_value)

if target_index != -1:
    print(f"{target_value}-ი არსებოს სორტირებულ სიაში ინდექსით {target_index}")
else:
    print(f"{target_value}-ი არ არსებობს სორტირებულ სიაში.")
