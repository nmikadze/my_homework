
#   თამაში : გამოიცანით რიცხვი
import json
import random                       #შემთხვევითი რიცხვის შემოტანა
from datetime import datetime       #თარიღის და დროის დასაფიქსირებლად
import tkinter as tk            
from tkinter import messagebox

def log_guess(guess):               # ფუნქცია, რომელიც ჩაწერს შეყვანილ რიცხვს და მის შეყვანის დროს JSON ფაილში
    now = datetime.now()            #მიმდინარე დროის ობიექტის შექმნა
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")        # დროის ფორმატის გადაწერა
    data = {"guess": guess, "timestamp": current_time}        # მონაცემების შექმნა

    with open("log.json", "a") as file:
        json.dump(data, file)                               # JSON ფაილში მონაცემების ჩაწერა
        file.write("\n")                                    # ახალ ხაზზე გადასვლის დამატება

# ფუნქცია, რომელიც შეამოწმებს შეყვანილ რიცხვს 
def guess_number():
    min_range = 1                                           # მინიმალური რიცხვი
    max_range = 5                                           # მაქსიმალური რიცხვი 
    target_number = random.randint(min_range, max_range)    # შემთხვევითი რიცხვი

    def check_guess():
        nonlocal target_number
        try:
            user_guess = int(entry.get())
            log_guess(user_guess)
            if user_guess < target_number:
                messagebox.showinfo("Result", "თქვენი შეყვანილი რიცხვი ჩაფიქრებულ რიცხვზე ნაკლებია!")
            elif user_guess > target_number:
                messagebox.showinfo("Result", "თქვენი შეყვანილი რიცხვი ჩაფიქრებულ რიცხვზე მეტია!")
            else:
                messagebox.showinfo("Result", f"გილოცავთ! თქვენ გამოიცანით ჩაფიქრებული რიცხვი: {target_number}")
        except ValueError:
            messagebox.showerror("Error", "აუცილებლად უნდა შეიყვანე რიცხვი (შესაბამის დიაპაზონში)!")
        entry.delete(0, tk.END)
# გრაფიკული ინტერფეისი
    root = tk.Tk()
    root.title("რიცხვის გამოცნობა")
    root.geometry("300x150")

    label = tk.Label(root, text=f"გთხოვთ შეიყვანოთ რიცხვი {min_range} დან {max_range} მდე:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="შემოწმება", command=check_guess)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    guess_number()

# ლოგის ბეჭვდა
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
