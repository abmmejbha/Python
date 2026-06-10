import getpass
database = {"abm": "0000", "mejbha": "1234"}

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i and password == database[i]:
        print("Login successful!")
        break
else:    print("Login failed! Please check your username and password.")
    