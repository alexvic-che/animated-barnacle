

opeos_results = {}
active = True

while active:

    name = input("What is ur name")
    mesto_otpuska = input("Mesto otpuska")
    opeos_results[name] = mesto_otpuska
    prodolzaem = input("Prodolzaem (y/n)")

    if prodolzaem == 'n':
        active = False

print(opeos_results)

