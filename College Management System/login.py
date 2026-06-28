from admin import admin_menu
from Faculty import faculty_menu
from Student import student_menu
def login():
    while True:
        print("*********  Welcome  *********")
        print("1.Admin")
        print("2.Faculty")
        print("3.Student")
        print("4.Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            admin_menu()
        elif choice == "2":
            faculty_menu()
        elif choice == "3":
            student_menu()
        else:
            print("Thank you")
            break
