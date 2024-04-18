book={"apples":1.65, "milk": 1.34, "avocado": 2.97 }



phonebook={}

phonebook["mum"]=134123412
phonebook["dsd"]=124124



voted={}

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote!")


cache = {}


graph={}
graph["you"] = ["alice","bob","claire", ]
graph["bob"] = ["anuj", "peggy"]

