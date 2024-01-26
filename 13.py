#დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
#########################################################################################################################

def write_to_file_until_enough():
    with open("output.txt", "w") as file:
        while True:
            user_input = input("შეიყვანეთ ტექსტი: ")
            file.write(user_input + "\n")
            if "enough" in user_input.lower():
                break

# 
write_to_file_until_enough()

# output.txt ფაილის კონტენტის წაკითხვა და ბეჭდვა
with open("output.txt", "r") as file:
    content = file.read()
    print(content)






#########################################################################################################################
# 2.დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.
#########################################################################################################################
    

import os

def create_file_in_location():
    user_location = input("შეიყვანეთ საქაღალდის ლოკაცია: ")
    user_filename = input("შეიყვანეთ შესაქმელი ფაილის სახელი: ")

    file_path = os.path.join(user_location, user_filename)

    with open(file_path, "w") as file:
        file.write("Hello, this is a new file!")

    print(f"ფაილი შეიქმნა {file_path}-ზე")

# ფუნქციის გამოძახება
create_file_in_location()

# საქაღალდეში არსებულ ყველა ფაილის სიას ამოიბეჭდება
location_files = os.listdir()
print(f"საქაღალდში არსებული ფაილები: {location_files}")
