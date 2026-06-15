print("Welcome to the tip calculator.")
bill=float(input("what was the total bill? "))
people=int(input("How many people to split the bill? "))
tip=int(input("what percentage tip would you like to give? 10,12, or 15? "))
pay=tip/100*bill +bill
print(pay)

print("BMI CALCULATOR.")
height=input("enter your height in m:")
weight=input("enter your weight in kg: ")
BMI=int(weight)/float(height) **2
print("YOUR BMI IS:", BMI)

print("round off the number 8/3", round(8/3,2))

print("AGE")
age=input("what is your current age?")
age_as_int = int(age)
years_remaining=90-age_as_int
days_remaining = years_remaining *365
weeks_remaining = years_remaining*52
months_remaining=years_remaining*12
msg=f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(msg)
