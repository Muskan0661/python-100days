num=int(input("enter num to find factorial."))
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)    

fact(num)        