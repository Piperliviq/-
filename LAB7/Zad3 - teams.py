class InvalidParameter(Exception):
    def __init__(self, name):
        self.name = name
        print(f"Invalid class parameter: {name}")


class InvalidAgeError(InvalidParameter):
    def __init__(self, age):
        super().__init__(age)
        self.age = age
        print(f"Invalid class parameter: {age}")


class InvalidSoundError(InvalidParameter):
    def __init__(self, sound):
        super().__init__(sound)
        print(f"Invalid class parameter: {sound}")


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if name != str:
            raise InvalidParameterError("name")
        elif age != int:
            raise InvalidAgeError
        elif sound != str:
            raise InvalidSoundError

    def make_sound(self):
        print((f"{name} says {sound}!"))

    def print(self):
        pass
    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError()
        elif sound.count('r') <= 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar({name}, {age}, {sound})")
    def daily_task(self, animals):
