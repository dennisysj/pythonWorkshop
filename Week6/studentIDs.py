import random

# Create an empty dictionary
students = {}

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists.")
    else:
        students[name] = random.randint(1000, 9999)
        print(f"{name} added with ID {students[name]}.") #f just means evaluate the expression inside the string, formats the output so you don't have to use commas or "+"'s

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(f"{name} removed.")
    else:
        print("Student not found.")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nCurrent students:")
        for name, sid in students.items():
            print(f" - {name}: {sid}")
        print()

def menu():
    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()
