class Student:
    def __init__(self, st_id, st_name, st_class):
        self.st_id = st_id
        self.st_name = st_name
        self.st_class = st_class

    def display(self):
            return f'student_id: {self.st_id}|student_name: {self.st_name}|student_class: {self.st_class}'
    
details = Student(102,'Ady','modern')
print(details.display())
