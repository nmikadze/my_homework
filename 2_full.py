#1.	ვიქტორინა შეადგინ ევიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც? ”სავარაუდო პასუხები:
#1.შუმერთა
#2.სელჩუკთა
#3.რომის
#4.მონღოლთა
#მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი. შეცდომის შემთხვევაში იბეჭდება: 
#„არა! სწორი პასუხი არომის!“
#სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!“


print (F"""
რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც? 
       
       სავარაუდო პასუხები:

        1.შუმერთა
        2.სელჩუკთა
        3.რომის
        4.მონღოლთა
 """)



Correct_answer1 = "Rome"
Correct_answer2 = "3"

answer = input ("დაწერე პასუხი ან მიუთითე ნომერი: ")
if (answer == Correct_answer1):
       print ("სწორია!")
elif (answer == Correct_answer2):
       print ("სწორია!")
else: 
       print ("არა! სწორი პასუხი არომის!")



# 2. ონლაინ მაღაზია 

print (F"""
აირჩიე კატეგორია:

1.ლეპტოპები
2.პერსონალური კომპიუტერები
3.მობილურები

       აირჩიე სასურველი პროდუქტის რიგითი ნომერი
 """)

leptop_1_price = 100
leptop_2_price = 500
leptop_3_price = 1000

pc_1_price = 200
pc_2_price = 700
pc_3_price = 1700


mob_1_price = 300
mob_2_price = 1300
mob_3_price = 2300



thing = int(input("აირჩიე სასურველი პროდუქტის რიგითი ნომერი: "))
if thing >= 3 :
    print ('ასეთი კატეგორია არ არსებობს')
else:
    max_price = int(input("შეიყვანე მაქსიმალური მისაღები ფასი: "))



if thing  == 1 and max_price < leptop_1_price :
    print ('ამ თანხაში არ გააჩნია შემოთავაზება')
elif thing  == 1 and max_price < leptop_2_price :
    print ("ამ თანხაში შეგიძლია შეიძინო ლეპტოპი #1 ")
elif thing  == 1 and max_price < leptop_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო ლეპტოპი #2 ")
elif thing  == 1 and max_price >= leptop_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო ლეპტოპი #3 ")

if thing  == 2 and max_price < pc_1_price :
    print ('ამ თანხაში არ გააჩნია შემოთავაზება')
elif thing  == 2 and max_price < pc_2_price :
    print ("ამ თანხაში შეგიძლია შეიძინო PC  #1 ")
elif thing  == 2 and max_price < pc_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო PC #2 ")
elif thing  == 2 and max_price >= pc_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო PC #3 ")

if thing  == 3 and max_price < mob_1_price :
    print ('ამ თანხაში არ გააჩნია შემოთავაზება')
elif thing  == 3 and max_price < mob_2_price :
    print ("ამ თანხაში შეგიძლია შეიძინო MOB #1 ")
elif thing  == 3 and max_price < mob_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო MOB #2 ")
elif thing  == 3 and max_price >= mob_3_price :
    print ("ამ თანხაში შეგიძლია შეიძინო MOB #3 ")





 #3. ქუესთი სშედგენა(Text Based Adventure Game)დაწერე ერთმანეთშ იჩასმულიi f-else კონსტრუქციების გამოყენებით 

print (F"""
საგნის სასწავლად უნდა აირჩიო ტრეინინგ ცენტრი:

1. Training center 1
2. Training center 2
2. Training center 3

 """)


training_center = input ("Choose a Training center from list : ")


if (training_center == "Training center 1"):
    print ("In Training center 1 you can learn only English. Do you really want to learn English?")
    answer = input ("Please, confirm y/n : ")
    if (answer == "y"):
        print ("Please contact us by Mail")
    elif (answer == "n"):
        print ("please Choose an other Training center from list:")

elif  (training_center == "Training center 2"):
    print ("In Training center 2 you can learn only English. Do you really want to learn German?")
    answer = input ("Please, confirm y/n : ")
    if (answer == "y"):
        print ("Please contact us by Mail German@German.de")
    elif (answer == "n"):
        print ("please Choose an other Training center from list:")



else:
    print ("In Training center 3 you can learn only Georgian. Do you really want to learn Georgian?")
    answer = input ("Please, confirm y/n : ")
    if (answer == "y"):
        print ("welcome to learn Georgian")
    elif (answer == "n"):
        print ("please Choose an other Training center from list:")


