# crete a function which store the student name, ID, Class, and subject.
# create another function which store the subject marks and display the result of particular student

class Student:
    def __init__(self, student_id, name, student_class):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.subject_marks = {}

def store_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    student_class = input("Enter class: ")
    student = Student(student_id, name, student_class)
    return student

def store_subject_marks(student):
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        marks = float(input(f"Enter {subject} marks for {student.name}: "))
        student.subject_marks[subject] = marks

def display_student_result(student):
    print(f"\nStudent ID: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Class: {student.student_class}")

    if student.subject_marks:
        print("\nSubject-wise Marks:")
        for subject, marks in student.subject_marks.items():
            print(f"{subject}: {marks}")
    else:
        print("\nNo subject marks available.") 

# instance:
if __name__ == "__main__":
    student1 = store_student_information()
    store_subject_marks(student1)
    display_student_result(student1)

# taking user input for multiple student to display the student result:

def store_student_details(num_students, num_subjects):
    student_details = {}
    for i in range(num_students):
        name = input("Enter student name: ")

        subject_marks = {}
        for j in range(num_subjects):
            subject = input("Enter subject name for {}: ".format(name))
            mark = float(input("Enter marks for {} in {}: ".format(name, subject)))
            subject_marks[subject] = mark

        student_details[name] = subject_marks
    return student_details

def display_subject_marks_for_student(student_details, target_name):
    if target_name in student_details:
        print("\nSubject marks for {}:".format(target_name))
        subjects = student_details[target_name]
        for subject, mark in subjects.items():
            print("Subject: {}, Marks: {}".format(subject, mark))
    else:
        print("Student not found.")

def main():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    student_details = store_student_details(num_students, num_subjects)

    target_name = input("Enter the student name to display subject marks: ")

    display_subject_marks_for_student(student_details, target_name)

if __name__ == "__main__":
    main()

    


    

