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

# Example Usage
if __name__ == "__main__":
    student1 = store_student_information()
    store_subject_marks(student1)
    display_student_result(student1)
    


    

