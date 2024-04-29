from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """Метод для возвращения pk"""

    def get_info(self):
        return "Базовый класс Model"

class ModelForm(Model):
    ID = 0
    def __init__(self,login, password):
        self._login = login
        self._password = password
        self._id = self.set_id()
    @classmethod
    def set_id(cls):
        cls.ID+=1
        return cls.ID
    def get_pk(self):
        return self._id

