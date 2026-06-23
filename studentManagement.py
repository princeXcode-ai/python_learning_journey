import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")

    student = {
        "name": name,
        "age": age,
        "roll": roll
    }

    students.append(student)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Roll: {s['roll']}")


def search_student(students):
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print(s)
            return

    print("Student not found.")


def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Save & Exit")


def main():
    students = load_students()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            save_students(students)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()