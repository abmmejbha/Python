# name = input("what is your name?")
# age = int(input("How old are you?"))
# height = float(input("How tall are you?"))

# age = age +1

# print("Hello " + name)
# print("You are " + str(age))
# print("You are " + str(height))


# import math 
# pi=3.14
# x=1
# y=2
# z=3


# print(math.ceil(pi))
# print(round(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(math.sqrt(400))
# print(max(x,y,z))
# print(min (x,y,z))


#slicing = create a substring by extracting elements from another
# string
# indexing[] or slice[]
# start:stop:step

name = "abm mejbha"
first_name = name[:3]
second_name = name[4:] #[4:10]

reversed_name = name[::-1]

print(first_name)
print(second_name)
print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(7, -4) #start from 7,  start from -4 backward

print(website1[slice])
print(website2[slice])

