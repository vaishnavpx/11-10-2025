class Person(object):
    def __init__(self,name,id_num):
        self.name=name
        self.id_num=id_num
    def display(self):
        print(self.name)
        print(self.id_num)

class Employee(Person):
    def __init__(self, name, id_num,salary,post):
        self.salary=salary
        self.post=post

        Person.__init__(self,name,id_num)

    def display2(self):
        print(self.salary)
        print(self.post)
        

a=Employee("Rahul",886012,200000,"Intern")

a.display()
a.display2()