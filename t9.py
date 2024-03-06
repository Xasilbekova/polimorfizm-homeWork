class University:
    def __init__(self, university) -> None:
        self.university = university

    def info(self):
        print(f"{self.university}")

class Staff(University):
    def __init__(self, university, first_name, last_name, age) -> None:
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
        print(f"{self.university}, {self.first_name}, {self.last_name}, {self.age}")
class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group) -> None:
        super().__init__(university, first_name, last_name, age)
        self.group = group
    
    def more_info(self):
        print(f"{self.university}, {self.first_name}, {self.last_name}, {self.age}, {self.group}")

class Teache(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject) -> None:
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def more_info(self):
        print(f"{self.university}, {self.first_name}, {self.last_name}, {self.position}, {self.subject}")

class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position) -> None:
        super().__init__(university, first_name, last_name, age)
        self.position = position

    def more_info(self):
        print(f"{self.university}, {self.first_name}, {self.last_name}, {self.position}")


university = University("CHDPU")
staf = Staff("CHDPU", "Surayyo", "Xasilbekova", 30)
student = Student("CHDPU", "Surayyo", "Xasilbekova", 30, "21/2")
teache = Teache("CHDPU", "Surayyo", "Xasilbekova", 30, "Active", "Subject")
otherStaff = OtherStaff("CHDPU", "Surayyo", "Xasilbekova", 30, "Active")

university.info()
staf.staff_info()
student.more_info()
teache.staff_info()
otherStaff.more_info()