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

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print(f"Hello my name is {self.name} {self.family}.", f"I'm {self.age} years old.",
              f"My nationality is {self.nationality}.", f"I teach in {self.university} from {self.experience} years.")


teachers = []

Bobi = Lecturer("Bobi", "Vaklinov", "32", "bulgarian", "SU", "5")
Moni = Lecturer("Moni", "Atanasova", "57", "portugal", "TU", "30")
Gosho = Lecturer("Gosho", "Pavlov", "45", "german", "UNSS", "15")

teachers.append(Bobi)
teachers.append(Moni)
teachers.append(Gosho)

Bobi.print()
Moni.print()
Gosho.print()

print(teachers)
