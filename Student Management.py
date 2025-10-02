import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_data(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_data()
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {"Roll": roll, "Name": name, "Age": age, "Course": course}
    students.append(student)
    save_data(students)
    print(" Student added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No records found.")
    else:
        for s in students:
            print(f"{s['Roll']} - {s['Name']} ({s['Age']} yrs) - {s['Course']}")

def search_student():
    students = load_data()
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["Roll"] == roll:
            print(f"Found: {s}")
            return
    print(" Student not found!")

def delete_student():
    students = load_data()
    roll = input("Enter Roll No to delete: ")
    students = [s for s in students if s["Roll"] != roll]
    save_data(students)
    print("✅ Record deleted successfully!")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
