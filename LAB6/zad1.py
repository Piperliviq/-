class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality


students = []

Bobi = Person("Bobi", "Vaklinov", "30", "bulgarian")
Moni = Person("Moni", "Atanasova", "25", "portugal")
Gosho = Person("Gosho", "Pavlov", "19", "german")

students.append(Bobi)
students.append(Moni)
students.append(Gosho)

print(f"Hello my name is {Bobi.name} {Bobi.family}.",f"I'm {Bobi.age} years old.",f"My nationality is {Bobi.nationality}.")
print(f"Hello my name is {Moni.name} {Moni.family}.",f"I'm {Moni.age} years old.",f"My nationality is {Moni.nationality}.")
print(f"Hello my name is {Gosho.name} {Gosho.family}.",f"I'm {Gosho.age} years old.",f"My nationality is {Gosho.nationality}.")


print(students)
