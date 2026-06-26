my_list = []

n = int(input("How many elements do you want to enter? "))

for i in range(n):
    item = input(f"Enter element {i+1}: ")
    my_list.append(item)

def length(lst):
    return len(lst)

print("Length of list:", length(my_list))