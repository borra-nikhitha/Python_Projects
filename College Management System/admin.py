def admin_menu():
    username = input("Enter admin username:")
    password = input("Enter password:")
    if username == "admin01" and password == "admin@01":
        print("Login Successful")
    else:
        print("Invalid details")
