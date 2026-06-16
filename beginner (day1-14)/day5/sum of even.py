sum=0
#method 1
for i in range(2,101,2):
    sum+=i
    
print(sum)        

#method 2
sum2=0
for i in range(1,101):
    if i%2==0:
        sum2+=i
    
print(sum2)        
