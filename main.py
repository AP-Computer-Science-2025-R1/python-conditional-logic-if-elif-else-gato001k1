username = "user"
password_length = 5

if username == "admin":
    if password_length >=10:
        print("Login successful")
    else: 
        print("Admin password incorrect.")
elif username == "user":
    if password_length >=6:
        print("Login successful")
    else:
        print("User password must be 6+ characters.")
