class Student:
    def __init__(self, name, email, phone_number, date_of_birth, course):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.course = course

    def __str__(self):
        return f"Student Name: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nDate of Birth: {self.date_of_birth}\nCourse: {self.course}"

students = []

def add_student():
    student_name = input("Enter student name: ")
    student_email = input("Enter student email: ")
    student_phone_number = input("Enter student phone number: ")
    student_date_of_birth = input("Enter student date of birth (YYYY-MM-DD): ")
    student_course = input("Enter student course: ")

    student = Student(student_name, student_email, student_phone_number, student_date_of_birth, student_course)
    students.append(student)

    print(f"Student {student_name} added successfully.")

def view_students():
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")

def remove_student():
    student_name = input("Enter student name to remove: ")

    found_student = False
    for i, student in enumerate(students):
        if student.name == student_name:
            students.pop(i)
            found_student = True
            break

    if found_student:
        print(f"Student {student_name} removed successfully.")
    else:
        print(f"Student {student_name} not found.")


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")

    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        remove_student()

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
