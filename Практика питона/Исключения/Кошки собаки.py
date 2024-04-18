file1 = "dogs.txt"
file2 = "cats.txt"

try:
    with open(file1) as f:
        content = f.read()
    print("Собаки")
    print(content.rstrip())
except FileNotFoundError:
    print("Файл не найден")


try:
    with open(file2) as f:
        content = f.read()
    print("Кошки")
    print(content.rstrip())
except FileNotFoundError:
    pass

