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






first_user = User('Egart' , 'kervich', 54, 'France')

first_user.describe_user()
first_user.greet_user()

second_user = User('Elena', 'PAvlovna', 44, 'Rusia')

second_user.describe_user()
second_user.greet_user()

print(second_user.login_attemps)
x=1
while x<5:
    second_user.increment_login_attemps()
    x+=1

print(second_user.login_attemps)

second_user.reset_login_attemps()
print(second_user.login_attemps)