print("leap year")
year=int(input("which year do you want to check for leap year?"))
if year%4==0:
    if year % 100==0:
        if year %400==0:
            print("leap year")
        else:
            print("not a leap year.")
    else:
        print("leap year.")
else:
    print("not a leap year.")
    
print("\n pizza delivery.")
print("welcome to python pizza delivery.")
size=input("what size pizza do you want ?( S,M,L)")
add_pep=input("do you want peproni? (Y,N) ")
extra_cheese=input("do you want extra cheese?")

bill=0
if size=="S":
    bill+=15
elif size== "M":
    bill+=20
else:
    bill+=25
            
if add_pep =="Y":
    if size=="S":
        bill+=2    
    else:
        bill+=3

if extra_cheese =="Y":
    bill+=1
    
print(f"your final bill is ${bill}")                            

print("love calculator.")
name1=input("what is your name? ")
name2=input("what is their name? ")

combine_string=name1+name2
lower_case_string=combine_string.lower()

t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true=t+r+u+e

l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")

love=l+o+v+e

love_score=int(str(true)+str(love))

print(love_score)

if (love_score < 10) or (love_score >90):
    print(f"your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >40) or (love_score <50):
    print(f"your love score is {love_score}, you are alright together.")

else:
    print(f"your score is {love_score}.")               

print("WELCOME TO TRESSURE ISLAND.")  
print("Your mission is to find the treasure.")  
direction=input("where do you want to go?(left or right) ").lower()
if direction=="right":
    print("game over.")
if direction=="left":
    action=input("want to swim or wait ?").lower()
    if action=="swim":
        print("game over.")
    else:
        door=input("which door? yellow,red or blue. ").lower()
        if (door=="red") or door=="blue":
            print("game over.")
        else:
            print("you win!")
            
                        
    