def faculty_menu():
    username = input("Enter Faculty Username:")
    password = input("Enter password:")
    if username == "Faculty01" and password == "Faculty!01":
        print("Login Successfull")
    else:
        print("Invalid details")
