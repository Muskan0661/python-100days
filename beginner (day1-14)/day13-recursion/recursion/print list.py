list=[1,2,3,4]

def display(elements, idx):
    if idx==len(elements):
        return 
    print(elements[idx])
    display(elements,idx+1)

display(list,0)