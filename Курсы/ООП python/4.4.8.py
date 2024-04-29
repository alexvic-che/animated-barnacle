class Aircraft:
    def __init__(self,model, mass, speed, top):
        self._model =model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == "_model" and type(value) != str:
            raise TypeError('неверный тип аргумента')
        if key == "_mass" and value <= 0:
            raise TypeError('неверный тип аргумента')
        if key == "_speed" and value <= 0:
            raise TypeError('неверный тип аргумента')
        if key == "_top" and value <= 0:
            raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == "_chairs" and (value <= 0 or type(value)!=int):
            raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key == "_weapons" and type(value) != dict:
            raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


a = PassengerAircraft('model', 1, 2, 3, 1.2)
planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
          ]