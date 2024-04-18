file = "learning_python.txt"

with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())
print("///////////////////////")
with open(file) as file_object:
    contents = file_object.read()
    print(contents)

with open(file) as object:
    lines = object.readlines()
string =""
for line in lines:
    string+=line

print("///////////////////////")
print(string)
print("///////////////////////")
print(string.replace("Python", "C"))

