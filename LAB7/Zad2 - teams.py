class InvalidParameterError(Exception):
    pass

class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)

        if type(carbs) is not float or type(protein) is not float or type(fats) is not float or type(salt) is not float:
            raise InvalidParameterError

        elif (self.carbs + self.protein + self.fats + self.salt) > 100:
            raise NutrientError

        elif carbs == 0 and protein == 0 and fats == 0 and salt == 0:
            raise InvalidFoodError

    def print_label(self):
        print(f"Food{self.carbs, self.protein, self.fats, self.salt}")

for i in range(0, 120, 10):
     try:
        Bread = Food(45.2, 1.5, 2.2, 1.8)

     except InvalidParameterError:
        print("Nutrients must be type float")
     except NutrientError:
        print("Nutrients can't be over 100")
     except InvalidFoodError:
        print("Nutrients can't be 0")
     else:
        Bread.print_label()


#tests
"""for i in range(0, 120, 10): 
    try:
        cake = Food(95.9, 1.5, 2.2, 1.8)

    except InvalidParameterError:
        print("Nutrients must be type float")
    except NutrientError:
        print("Nutrients can't be over 100")
    except InvalidFoodError:
        print("Nutrients can't be 0")
    else:
        cake.print_label()

for i in range(0, 120, 10):
    try:
        cola = Food(0.0, 0.0, 0.0, 0.0)

    except InvalidParameterError:
        print("Nutrients must be type float")
    except NutrientError:
        print("Nutrients can't be over 100")
    except InvalidFoodError:
        print("Nutrients can't be 0")
    else:
        cola.print_label()

for i in range(0, 120, 10):
    try:
        milka = Food(40, 0.0, 0.0, 0.0)

    except InvalidParameterError:
        print("Nutrients must be type float")
    except NutrientError:
        print("Nutrients can't be over 100")
    except InvalidFoodError:
        print("Nutrients can't be 0")
    else:
        milka.print_label()"""