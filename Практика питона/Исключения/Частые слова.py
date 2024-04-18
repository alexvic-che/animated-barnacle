file ='Myths of northern lands : Narrated with special reference to literature and'

def the_in_text(file):
    with open(file) as f:
        lines = f.readlines()
    string =""
    for line in lines:
        string+=line
    print(string.lower().count('the '))

the_in_text(file)