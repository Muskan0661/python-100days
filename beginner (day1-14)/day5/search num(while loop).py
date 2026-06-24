numbers = []
i = 1

while i <= 10:
    numbers.append(i * i)
    i += 1

print(numbers)

search = int(input("Enter number you want to search: "))

idx = 0
while idx < len(numbers):
    if numbers[idx] == search:
        print("Found at index", idx)
        break
   
    else:
        print("finding..")
    idx += 1
print("end of loop.")         
        