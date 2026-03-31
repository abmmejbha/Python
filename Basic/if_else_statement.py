temp = int(input("What is the temperature today?"))

# if temp>=0 and temp<= 30:
#     print("the temperature is good today")
#     print("You can go outside")
# elif temp < 0 or temp >30:
#     print("the temprature is bad today")
#     print("stay inside")
    

lala = (input("What is your name?"))

# not logical operator

if not(temp >=0 and temp <= 30):
    print("the temperature is bad today")
    print("stay inside")
elif not(temp < 0 or temp >30):
    print("the temperature is good today")
    print("You can go outside")
    
print("hello " + lala + " lala" )

name = input("What is your name?")
age = int(input("How old are you?"))
height= float(input("How tall are your?"))

print("You are "+ name)
print("You are "+ str(age)+"years old")
print("You height is "+ str(height))

name = "abm mejbha"

#reverse a string
reversed_name = name[::-1]
print(reversed_name)


