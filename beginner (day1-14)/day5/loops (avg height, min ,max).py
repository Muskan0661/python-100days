height = input("Enter list of students' heights: ").split()

total_height = 0
for i in height:
    total_height += int(i)

length = len(height)

avg = round(total_height / length)
print(f"Average height of students is: {avg}")

# Convert heights to integers

high_height = int(height[0])
low_height = int(height[0])

for h in height:
    h=int(h)
    if h > high_height:
        high_height = h
    if h < low_height:
        low_height = h

print(f"Highest height in class is: {high_height}")
print(f"Lowest height in class is: {low_height}")