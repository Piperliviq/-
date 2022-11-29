class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Hello my name is {self.name} {self.family}.", f"I'm {self.age} years old.",
              f"My nationality is {self.nationality}.")

students = []

Bobi = Person("Bobi", "Vaklinov", "30", "bulgarian")
Moni = Person("Moni", "Atanasova", "25", "portugal")
Gosho = Person("Gosho", "Pavlov", "19", "german")

students.append(Bobi)
students.append(Moni)
students.append(Gosho)

Bobi.print()
Moni.print()
Gosho.print()

print(students)
