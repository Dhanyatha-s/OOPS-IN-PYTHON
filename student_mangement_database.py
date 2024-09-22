class Student:
    def __init__(self, name, rollno, m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # accept new students
    def accept(self, Name, Rollno, marks1, marks2):

        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

    # Display students with the details
    def display(self, ob):
        print("Name:", ob.name)
        print("Roll Number:", ob.rollno)
        print("Marks 1:", ob.m1)
        print("Marks 2:", ob.m2)
        print("\n")

    # search students details with roll number
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
            
    #update the student details
    def update(self, rn, No):
        i = su.search(rn)
        roll = No
        ls[i].rollno = No

    # delete the detsils of student
    def delete(self, rn):
        i= su.search(rn)
        del ls[i]
        print( f"the student {i} details has been deleted")

ls = []
su = Student('', 0,0,0)

print("the database contains list of student details")
print("can add, del,display search and update")

su.accept("Karan", 2,20,40)
su.accept("vayu", 2, 56,67)
su.accept("murag", 3, 59,47)

for i in range(ls.__len__()):
    su.display(ls[i])


s= su.search(3)
su.display(ls[s])

su.delete(2)
print(ls.__len__())
for i in range(ls.__len__()):
    su.display(ls[i])

su.update(3,2)
print(ls.__len__())
for i in range(ls.__len__()):
    su.display(ls[i])