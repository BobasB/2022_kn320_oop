class Rocket:
    def __init__(self, name:str, mass) -> None:
        assert name.isascii(), "Значення name повинно містити символи таблиці ASCII"
        assert mass >= 0, "Масса Ракети має бути не 0!"
        self.name = name
        self.mass = mass
        ## Можна ассерт замінити на IF, але це не дуже правильно
        #if isinstance(mass, float):
        #    self.mass = mass
        #else:
        #    raise AssertionError("Маса має бути введена цифрами")
    
    @property
    def get_mass(self):
        return f"Ракета {self.name} має масу {self.mass} кг."

    def convert_to_pounds(self): #конвертуємо кг в фунти
        if self.mass > 0:
            return self.mass * 2.20462262
        return None  
    
    def new_fun(self):
        return f"Not tested"

def test_pass():
    a = Rocket("Falcon 9", 549054.0)
    assert "Falcon 9" in a.get_mass, "Назва ракети не коректно виводиться"
    #print()
    #a.mass = -10
    #print(a.convert_to_pounds())
    #print(f"Маса ракети в фунтах {a.convert_to_pounds()}")

