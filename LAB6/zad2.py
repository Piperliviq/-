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

students = []

Bobi = Student("Bobi", "Vaklinov", "30", "bulgarian", "SU", "first")
Moni = Student("Moni", "Atanasova", "25", "portugal", "TU", "second")
Gosho = Student("Gosho", "Pavlov", "19", "german", "UNSS", "third")

students.append(Bobi)
students.append(Moni)
students.append(Gosho)

print(f"Hello my name is {Bobi.name} {Bobi.family}.",f"I'm {Bobi.age} years old.",f"My nationality is {Bobi.nationality}.", f"I study in {Bobi.university}. This is my {Bobi.yearofstudy} year.")
print(f"Hello my name is {Moni.name} {Moni.family}.",f"I'm {Moni.age} years old.",f"My nationality is {Moni.nationality}.", f"I teach in {Moni.university}. This is my {Moni.yearofstudy} year.")
print(f"Hello my name is {Gosho.name} {Gosho.family}.",f"I'm {Gosho.age} years old.",f"My nationality is {Gosho.nationality}.", f"I teach in {Gosho.university}. This is my {Gosho.yearofstudy} year.")

print(students)
