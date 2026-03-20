class Student:
    count = 0
    
    def __init__(self, name, student_id, course_name):
        self.name = name
        self.student_id = student_id
        self.course_name = course_name
        
        Student.count += 1
    
    def show(self):
        print(f"name: {self.name}")
        print(f"student_id: {self.student_id}")
        print(f"course_name: {self.course_name}")
        
    
    @classmethod
    def total_number(cls):
        print(f"the number of students: {cls.count}")
        return cls.count

student1 = Student('Tom', '000001', 'Python programming')
student2 = Student('Jerry', '000002', 'Mathematics')
student3 = Student('Henry', '000003', 'Physics')

if __name__ == "__main__":
    print("students information:")
    student1.show()
    student2.show()
    student3.show()
    
    Student.total_number()
