class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class SchoolClass:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classes = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_class(self, class_name, teacher):
        new_class = SchoolClass(class_name, teacher)
        self.classes.append(new_class)

    def assign_student_to_class(self, student, class_name):
        for school_class in self.classes:
            if school_class.name == class_name:
                school_class.add_student(student)
                print(f"The student {student.name} is assigned to {class_name}")
                return
        print(f"Class {class_name} not found")

    def assign_teacher_to_class(self, class_name, teacher):
        for school_class in self.classes:
            if school_class.name == class_name:
                school_class.teacher = teacher
                print(f"Teacher {teacher.name} is assigned to {class_name}")
                return
        print(f"Class {class_name} not found")

    def student_info(self, student_name):
        for student in self.students:
            if student.name == student_name:
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                return
        print(f"Student {student_name} not found")

    def teacher_info(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                print(f"Name: {teacher.name}")
                print(f"Subject: {teacher.subject}")
                return
        print(f"Teacher {teacher_name} not found")

    def class_info(self, class_name):
        for school_class in self.classes:
            if school_class.name == class_name:
                print(f"Class Name: {school_class.name}")
                print(f"Teacher: {school_class.teacher.name}")
                print("Students: ")
                for student in school_class.students:
                    print(student.name)
                return
        print(f"Class {class_name} not found")

def main():
    school = School()
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Class")
        print("4. Assign Student to Class")
        print("5. Assign Teacher to Class")
        print("6. View Student Info")
        print("7. View Teacher Info")
        print("8. View Class Info")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            new_student = Student(name, age, grade)
            school.add_student(new_student)
        elif choice == '2':
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            new_teacher = Teacher(name, subject)
            school.add_teacher(new_teacher)
        elif choice == '3':
            class_name = input("Enter class name: ")
            teacher_name = input("Enter teacher name: ")
            teacher = next((t for t in school.teachers if t.name == teacher_name), None)
            if teacher:
                school.add_class(class_name, teacher)
            else:
                print("Teacher not found")
        elif choice == '4':
            student_name = input("Enter student name: ")
            class_name = input("Enter class name: ")
            student = next((s for s in school.students if s.name == student_name), None)
            if student:
                school.assign_student_to_class(student, class_name)
            else:
                print("Student not found")
        elif choice == '5':
            teacher_name = input("Enter teacher name: ")
            class_name = input("Enter class name: ")
            teacher = next((t for t in school.teachers if t.name == teacher_name), None)
            if teacher:
                school.assign_teacher_to_class(class_name, teacher)
            else:
                print("Teacher not found")
        elif choice == '6':
            student_name = input("Enter student name: ")
            school.student_info(student_name)
        elif choice == '7':
            teacher_name = input("Enter teacher name: ")
            school.teacher_info(teacher_name)
        elif choice == '8':
            class_name = input("Enter class name: ")
            school.class_info(class_name)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

