def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'enstein',
                             location='princeton',
                             field = 'physics')
print(user_profile)

my_profile = build_profile('sasha', 'pupkin',
                           age = '23',
                           city = 'Moskou',
                           weght = '144')

print(my_profile)