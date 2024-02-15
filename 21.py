
#   თამაში : გამოიცანით რიცხვი


import json
import random   #შემთხვევითი რიცხვის შემოტანა
from datetime import datetime   #თარიღის და დროის დასაფიქსირებლად

def log_guess(guess):   # ფუნქცია, რომელიც ჩაწერს შეყვანილ რიცხვს და მის შეყვანის დროს JSON ფაილში
    now = datetime.now()    #მიმდინარე დროის ობიექტის შექმნა
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")     # დროის ფორმატის გადაწერა
    data = {"guess": guess, "დრო:": current_time}       # მონაცემების შექმნა

    with open("log.json", "a") as file:
        json.dump(data, file)   # JSON ფაილში მონაცემების ჩაწერა
        file.write("\n")        # ახალ ხაზზე გადასვლის დამატება

# ფუნქცია, რომელიც შეამოწმებს შეყვანილ რიცხვს 

def guess_number():
    min_range = 1       # მინიმალური რიცხვი
    max_range = 5       # მაქსიმალური რიცხვი 
    target_number = random.randint(min_range, max_range)    # შემთხვევითი რიცხვი

    try:
        while True:
            user_guess = int(input(f"გამოიცანი რიცხვი {min_range} -დან   {max_range} -მდე შუალედში: "))
            log_guess(user_guess)       # შეყვანილი რიცხვის ჩაწერა log.json ფაილში

            if user_guess < target_number:
                print(f"""
                      ვერ გამოიცანი! ცადე უფრო დიდი რიცხვი.
                      """)
            elif user_guess > target_number:
                print(f"""
                      ვერ გამოიცანი! ცადე უფრო პატარა რიცხვი.
                      """)
            else:
                print(f"""
                      გილოცავთ! თქვენ გამოიცანით ჩაფიქრებულირიცხვი! ჩაფიქრებული რიცხვი იყო: {target_number}
                      """)
                break

    except ValueError:
        print(f"""
              აუცილებლად უნდა შეიყვანე რიცხვი  {min_range} -დან   {max_range} -მდე შუალედში:
              """)

    except Exception as e:
        print(f"შეცდომაა: {e}")

    finally:
        print(f"""
              თამაში დასრულებულია!
              """)

if __name__ == "__main__":
    guess_number()

def print_log():
    try:
        with open("log.json", "r") as file:
            data = file.readlines()
            print("რიცხვის გამოცნობა მოხდა შემდეგი მიმდევრობით:")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print("ლოგ ფაილი ვერ მოიძებნა.")
    except Exception as e:
        print(f"შეცდომა: {e}")

if __name__ == "__main__":
    guess_number()
    print_log()

        