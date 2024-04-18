class PhoneBook:
    def __init__(self):
        self.phone_numbers = []
    def add_phone(self, phone):
        self.phone_numbers.append(phone)

    def remove_phone(self, indx):
        del self.phone_numbers[indx]

    def get_phone_list(self):
        return self.phone_numbers

class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
