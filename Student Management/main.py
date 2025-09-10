from student_functions import (
    load_students,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)


def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():

    students = load_students() 

    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            students = add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students) 
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break 
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()