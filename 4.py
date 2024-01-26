#1. მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემულ იწინადადებაში. შედეგი დაბეჭდე. გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები. 
####################################################################################################################

user_input = input("შეიყვანეთ ტექსტი: ")

def analyze_information(user_input):
    total_numbers = 0
    total_letters = 0
    total_other_symbols = 0

    for char in user_input:
        if char.isdigit():
            total_numbers += 1
        elif char.isalpha():
            total_letters += 1
        else:
            total_other_symbols += 1

    print(f"რიცხვები: {total_numbers}")
    print(f"ანბანის ასოები: {total_letters}")
    print(f"სხვა სიმბოლოები: {total_other_symbols}")



analyze_information(user_input)

####################################################################################################################
#2.მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე, შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვებ ამეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.
####################################################################################################################


sentence1 = input("შეიყვანე პორველი წინადადება: ")
sentence2 = input("შეიყვანე მეორე წინადადება: ")


def create_third_sentence(sentence1, sentence2):

    if not sentence1 or not sentence2:
        
        return "Please enter valid sentences."

    
    first_char_sentence1 = sentence1[0]
    last_char_sentence2 = sentence2[-1]
    second_char_sentence1 = sentence1[1]
    last_char_sentence2 = sentence2[-1]


    third_sentence = f"{first_char_sentence1}{last_char_sentence2}{second_char_sentence1}{last_char_sentence2}"
    
    
    return third_sentence


result = create_third_sentence(sentence1, sentence2)
print("სიტყვა იქნება:", result)
# ასოების მიმდევრობა შევადგენინე. წინადადება ვერ მოვიფიქრე როგორ უნდაგააკეთოს. ანუ ასოების მიმდევრობა რომელიც დასრულებულ ახრს გამოხატავს როგორ უნდა შევადგენინო ვრ ვხვდები





###################################################################################################################
#3.მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორეწინადადებაში და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში. თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:„Strings are balanced!“ თუ რომელიმე პირობა დაირღვა, დაბეჭდე:„Strings are not balanced!“
####################################################################################################################


sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")


def check_balance(sentence1, sentence2):

    if sentence1[0] in sentence2 and sentence2[0] in sentence1:
        # Check if all characters of the second sentence are in the first sentence
        if all(char in sentence1 for char in sentence2):
            return "Strings are balanced!"
        else:
            return "Strings are not balanced!"
        

result = check_balance(sentence1, sentence2)
print(result)