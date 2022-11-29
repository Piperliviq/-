class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
            print(f"Hello my name is {self.name} {self.family}.",f"I'm {self.age} years old.",f"My nationality is {self.nationality}.", f"I study in {self.university}. This is my {self.yearofstudy} year.")


students = []

Bobi = Student("Bobi", "Vaklinov", "30", "bulgarian", "SU", "first")
Moni = Student("Moni", "Atanasova", "25", "portugal", "TU", "second")
Gosho = Student("Gosho", "Pavlov", "19", "german", "UNSS", "third")

students.append(Bobi)
students.append(Moni)
students.append(Gosho)

Bobi.print()
Moni.print()
Gosho.print()

print(students)
