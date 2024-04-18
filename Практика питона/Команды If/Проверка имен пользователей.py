current_users = ['admin', 'aboba', 'John' ,'boil' ,'goil']
current_users_title = []
for current_user in current_users:
    current_users_title.append(current_user.title())

print(current_users_title)

new_users = ['admin', 'gorg', 'JOHN' ,'golginm' ,'goil']
new_users_title = []
for new_user in new_users:
    new_users_title.append(new_user.title())

print(new_users_title)

for new_user in new_users_title:
    if new_user in current_users_title:
        print(f"Это имя,{new_user},пользователя уже занято")
    else:print(f"Это имя ,{new_user}, свободно")


