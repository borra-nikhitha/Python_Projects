def student_menu():
    username = input("Enter Student Username:")
    password = input("Enter password:")
    if username == "Student01" and password == "Student#01":
        print("Login Successfull")
    else:
        print("Invalid Details")
