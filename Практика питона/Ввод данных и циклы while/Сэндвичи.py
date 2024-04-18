sandwich_orders = ['first_sandvic','pastrami', 'second_asdq', 'pastrami','third_dasd', 'pastrami']
finished_sandvich = []
print("Pastrami bolse net")

while sandwich_orders:

    created = sandwich_orders.pop(0)
    if created =="pastrami":
        continue
    else:
        print(f"I made u a {created}")
        finished_sandvich.append(created)

print(finished_sandvich)


