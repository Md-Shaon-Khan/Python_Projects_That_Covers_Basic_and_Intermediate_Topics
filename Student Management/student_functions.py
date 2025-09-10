import json
import os

FILE_PATH = "D:\\Python Based Mini Project\\Student Management\\students.json"

def load_students():
    if not os.path.exists(FILE_PATH):
       return []
    
    try:
        with open(FILE_PATH,"r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except(json.JSONDecodeError, FileNotFoundError):
        return []

def save_students(students):
    with open(FILE_PATH,"w") as f:
        json.dump(students,f,indent=4)

def add_student(students):
    name =  input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Error: Roll number already exists!")
            return students
        
    age = input("Enter age: ").strip()
    dept = input("Enter department: ").strip()

    student = {
        "name": name,
        "roll": roll,
        "age" : age,
        "department": dept
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")
    return students

def view_students(students):
    if not students:
        print("No students found.")
        return
    
    print("\n---Student List---")
    for s in students:
        print(f"Name:{s['name']}, Roll:{s['roll']},Age:{s['age']},Dept:{s['department']}")

def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for s in students:
        if s["roll"] == roll:
            print(f"Found -> Name:{s['name']}, Roll: {s['roll']}, Age: {s['age']}, Dept: {s['department']}")
            return
    print("Student not found!")

def update_student(students):
    roll = input("Enter roll number to update: ").strip()
    for s in students:
        if s["roll"] == roll:
            print("Leave blank to keep existing value.")

           
            new_name = input(f"Enter new name ({s['name']}): ").strip()
            new_age = input(f"Enter new age ({s['age']}): ").strip()
            new_dept = input(f"Enter new department ({s['department']}): ").strip()

            if new_name: 
                s['name'] = new_name
            if new_age: 
                s['age'] = new_age
            if new_dept: 
                s['department'] = new_dept

            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found!")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found!")