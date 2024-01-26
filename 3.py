#1. ჯეირანის პროგრამა 
# დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით. თამაშის დასასრულებლად რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.


import random
 
data = ["ქვა", "ქაღალდი", "მაკრატელი"]
 
Man_score = 0
comp_score = 0
 
while Man_score <3 and comp_score < 3:
    Man_choice = input("Enter you choice (ქაღალდი, მაკრატელი, ქვა): ").lower().strip()
    if Man_choice not in data:
        continue
    else:
        comp = random.choice(data)
 
        Man_win1 = Man_choice == "ქაღალდი" and comp == "ქვა"
        Man_win2 = Man_choice == "მაკრატელი" and comp == "ქაღალდი"
        Man_win3 = Man_choice == "ქვა" and comp == "მაკრატელი"
 
        if Man_choice == comp:
            print("Draw!")    
            continue


        elif Man_win1 or Man_win2 or Man_win3:
            print("Man +1")    
            Man_score += 1
        
        
        else:
            print("Computer +1")    
            comp_score += 1
 
print(f"""
Man Score: {Man_score}
Computer Score: {comp_score}
""")

#############################################################################################
#2. გამრავლების ტაბულა გამრავლების ტაბულა
# ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.


print ("""
       გ ა მ რ ა ვ ლე ბ ი ს    ტ ა ბ უ ლ ა
       """)
for x in range(1, 11): 
    for y in range(1, 11): 
        print(x * y, end="\t")

    print("\n")


#############################################################################################


# 3. საბანკო ანგარიში
# შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარის ოდენობით. პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს. შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე, პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.


SUM = 300  # Removed unnecessary 'int' conversion

print("გაწეული ხარჯი?")

while SUM > 0:
    charge = int(input("ხარჯი: "))
    if charge > SUM :
        print ("ანგარიშზე არ არის საკმარისი თანხა")
    SUM = SUM - charge
    print(SUM)  # Fixed variable name from 'sum' to 'SUM'
    
    if charge == 0:
        break

#################################################################################################
# 4. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”

print("User Said Whaaat?")

while True: 
    word = str(input("Input word: "))
    print("User Said Whaaat?")
    print("User Said", word) 
    
    if word.lower() == "quit":  
        break  