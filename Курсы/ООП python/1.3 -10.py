class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()

a_dict = p1.__dict__

if a_dict:
    for a in a_dict:
        print(a)
        if a == 'job':
            print('True')
        else:
            print('False')
else: print(False)
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)
