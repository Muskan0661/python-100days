import math
def data(h, w,coverage):
    area=h*w
    num_of_cans=math.ceil(area/coverage)
    print(num_of_cans)
    

test_h=int(input("height of wall: "))
test_w=int(input("width of wall: "))
coverage=5
print(f"you will need {data(test_h, test_w,5)} of cans")
    