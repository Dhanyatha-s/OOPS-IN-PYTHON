class Employee:
    def __init__(self, role, dept, salary) -> str:
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Details of emp1 is :") 
        print("Role: ",self.role)
        print("Department: " ,self.dept)
        print("Salary: " ,self.salary)

class Engineer(Employee):
    def __init__(self, name, age) -> str:
        self.name = name
        self.age = age
        super().__init__("Engineering", "IT", "1000000")


engg1 = Engineer("Elena","23")
engg1.showDetails()