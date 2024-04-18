m = list(map(int, input().split()))
if m[0] == 1:
    if m[1] == 1:
        print("12.31", "01.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print("01.30", "02.01")
elif m[0] == 2:
    if m[1] == 1:
        print("01.31", "02.02")
    elif 2 <= m[1] <= 27:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 28:
        print("02.27", "03.01")
elif m[0] == 3:
    if m[1] == 1:
        print("02.28", "03.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print("03.30", "04.01")
elif m[0] == 4:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.31", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 29:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 30:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 5:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.30", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 6:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.31", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 29:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 30:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 7:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.30", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 8:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.31", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 9:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.31", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 29:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 30:
        print(f"0{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 10:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.30", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print(f"{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 11:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.31", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 29:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 30:
        print(f"{m[0]}.{str(m[1]-1).rjust(2, '0')}", f"{str(m[0]+1).rjust(2, '0')}.01")
elif m[0] == 12:
    if m[1] == 1:
        print(f"{str(m[0]-1).rjust(2, '0')}.30", f"{str(m[0]).rjust(2, '0')}.02")
    elif 2 <= m[1] <= 30:
        print(f"{str(m[0]).rjust(2, '0')}.{str(m[1]-1).rjust(2, '0')} {str(m[0]).rjust(2, '0')}.{str(m[1]+1).rjust(2, '0')}")
    elif m[1] == 31:
        print(f"{m[0]}.{str(m[1]-1).rjust(2, '0')}", "01.01")