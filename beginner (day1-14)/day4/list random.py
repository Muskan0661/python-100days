import random

n = input("Write names of group members: ")
names = n.split(", ")

pay = random.choice(names)

print(pay + " is going to pay the bill today!")