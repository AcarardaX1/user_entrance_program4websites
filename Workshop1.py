print("""
***********
User Entrance Progress            
***********      
""")

sys_username = "admin"
sys_password = "123456"

accession = 3

while True:
    username = input("Username: ")
    password = input("Password: ")
    if (username != sys_username and password == sys_password):
        print("Username is wrong!")
        accession -= 1
    elif (username == sys_username and password != sys_password):
        print("Password is wrong!")
        accession -= 1
    elif (username != sys_username and password != sys_password):
        print("Username and/or Password is wrong!")
        accession -= 1
    else:
        print("Welcome to the system!")
        break
    if (accession == 0):
        print("You have entered the wrong username and/or password 3 times. Please try again later.")
        break