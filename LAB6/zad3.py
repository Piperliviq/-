class Lecture:
    def __init__(self, university, experience):
        super().__init__()
        self.university = university
        self.experience = experience


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

teachers = []

Bobi = Lecturer("Bobi", "Vaklinov", "32", "bulgarian", "SU", "5")
Moni = Lecturer("Moni", "Atanasova", "57", "portugal", "TU", "30")
Gosho = Lecturer("Gosho", "Pavlov", "45", "german", "UNSS", "15")

teachers.append(Bobi)
teachers.append(Moni)
teachers.append(Gosho)

print(f"Hello my name is {Bobi.name} {Bobi.family}.",f"I'm {Bobi.age} years old.",f"My nationality is {Bobi.nationality}.", f"I teach in {Bobi.university} from {Bobi.experience}years.")
print(f"Hello my name is {Moni.name} {Moni.family}.",f"I'm {Moni.age} years old.",f"My nationality is {Moni.nationality}.", f"I teach in {Moni.university} from {Moni.experience}years.")
print(f"Hello my name is {Gosho.name} {Gosho.family}.",f"I'm {Gosho.age} years old.",f"My nationality is {Gosho.nationality}.", f"I teach in {Gosho.university} from {Gosho.experience}years.")


print(teachers)
