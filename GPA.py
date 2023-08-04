print("in the name of Allah")
name = input("whats your name : ") 
family = input("whats your family : ")

score1 = int(input("whats your score1 : "))
score2 = int(input("whats your score2 : "))
score3 = int(input("whats your score3 : "))
GPA = (score1 + score2 + score3)/3

if score1 > 20 or score1 < 0 :
    print("wrong please enter score1 between 0 to 20")
if score2 > 20 or score2 < 0 :
    print("wrong please enter score2 berween 0 to 20 ")
if score3 > 20 or score3 < 0 :
    print("wrong please enter score3 berween 0 to 20 ")
    
else :
        print(GPA)
    
if GPA > 18 :
    print("good score")
if GPA >= 10 :
    print("try harder ")
if GPA < 10 :
    print("Unacceptable")
print("good luck")