def name(first_name, last_name):
    
    if first_name=="" or last_name=="":
        return "you didn't provide valid inputs."
    first_name=first_name.title()
    last_name=last_name.title()
    return f"result: {first_name} {last_name}"

f_name=input("what is your first name? ")
l_name=input("what is your last name? ")
print(name(f_name,l_name))