class Person:
    platform = 'UNIVERSITY'

    def __init__(self, name: str, id: int, email: str, phone: str) -> None:
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone

    def __repr__(self) -> str:
        return f'Person(Name = {self.name}, id = {self.id}, E-mail = {self.email}, Phone = {self.phone})'
  # Student Class  
class Student(Person):
    def __init__(self, name: str, id: int, email: str, phone: str, department: str, batch: str) -> None:
        self.deparment = department
        self.batch = batch
        super().__init__(name, id, email, phone)

    def __repr__(self) -> str:
        #return f'Id: {self.id}, Name: {self.name}, E-mail: {self.email}, Phone: {self.phone}, Department: {self.deparment}, Batch: {self.batch}'

        info = "========Information for the Student: ========\n"
        info += f'Name: {self.name}\n'
        info += f'Id: {self.id}\n'
        info += f'E-mail: {self.email}\n'
        info += f'Phone: {self.phone}\n'
        info += f'Department: {self.deparment}'
        info += f'Batch: {self.batch}\n'
        return info
class Teacher(Person):
    def __init__(self, name: str, id: int, email: str, phone: str, subject: str) -> None:
        self.subject = subject
        super().__init__(name, id, email, phone)

    def __repr__(self) -> str:
        #return f' Id: {self.id}\n Name: {self.name}\n E-mail: {self.email}\n Phone: {self.phone}\n Subject: {self.subject}\n\n'

        info = "========Information for the Teacher: ========\n"
        info += f'Name: {self.name}\n'
        info += f'Id: {self.id}\n'
        info += f'E-mail: {self.email}\n'
        info += f'Phone: {self.phone}\n'
        info += f'Subject: {self.subject}\n'
        return info
p1 = Student("Tawhid Shakil", 15, "astalukdar39@gmail.com", "01770590639", "Software", "3rd")
print(p1)

t1 = Teacher("Al Akram", 4445, "alakram123@gmail.com", "017543353", "PPD")
print(t1)