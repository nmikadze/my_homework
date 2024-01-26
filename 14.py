
######################################################################################################################
# 1. დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
######################################################################################################################

def find_second_most_common_word(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

            # წაშალოთ ყველაზე ხშირად გამოყენებული სიტყვა
            most_common_word = max(word_count, key=word_count.get)
            words.remove(most_common_word)

            # მოიძებნოს მეორე ყველაზე ხშირად გამოყენებული სიტყვა
            second_most_common_word = max(word_count, key=word_count.get)
            return second_most_common_word
    except Exception as e:
        print(f"შეცდომა: {e}")
        return None

# ფუნქციის გამოძახება
file_path = r'D:\PYTHON\article.txt'
second_most_common_word = find_second_most_common_word(file_path)

if second_most_common_word is not None:
    print(f"იპოვება მეორე ყველაზე ხშირად განმეორებადი სიტყვა: {second_most_common_word}")
else:
    print("მეორე ყველაზე ხშირად განმეორებადი სიტყვა ვერ იპოვა.")

######################################################################################################################
#2. names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
######################################################################################################################
import shutil

def copy_csv_to_txt(csv_file, txt_file):
    try:
        shutil.copy(csv_file, txt_file)
        print(f"ინფორმაცია წარმატებით კოპირდა {txt_file}-ში.")
    except Exception as e:
        print(f"შეცდომა: {e}")

# ფუნქციის გამოძახება
csv_file_path = r'D:\PYTHON\names.csv'
txt_file_path = r'D:\PYTHON\names.txt'
copy_csv_to_txt(csv_file_path, txt_file_path)


######################################################################################################################


