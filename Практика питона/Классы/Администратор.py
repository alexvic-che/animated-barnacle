class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attemps = 0

    def describe_user(self):
        print(f"User_Info:\n first_name:{self.first_name.title()}\n last_name: {self.last_name.title()} \n "
              f"age: {self.age} \n country: {self.country.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name.title()}")

    def increment_login_attemps(self):
        self.login_attemps+=1

    def reset_login_attemps(self):
        self.login_attemps = 0

class Priveleges():
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Priveleges()


#
# admin = Admin('Andrie', 'Mira', 24, 'barselona')
#
# admin.privileges.show_privileges()