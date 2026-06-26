

def convert():
    if user=='usd':
        p=float(input("enter pakistani rupees to convert into  used ."))
        usd=p/280
        print(f"USD={usd:.2f}")    
    elif user=='pak':
        us=float(input("enter us dollars to convert into pakistani rupees."))
        paki=us*280
        print(f"PKR = {paki:.2f}")  
      
    else:
        print("wrong input.")            

while True:
    user=input("if you want to convert USD TO PAK TYPE 'PAK' , FOR PAK TO USD TYPE 'USD' .").lower()

    convert()
    
    again=input("do you want to convert again type 'yes' or 'no'. ")
    if again=="no":
        print("thankyou for using the currency converter!.")
        break
    