from collections import deque
graph={}
graph["you"] = ["alice", "bob", "claire", ]
graph["bob"] = ["anum", "peggy"]
graph["alice"]=[]
graph["claire"]=[]
graph["anum"]=[]
graph["peggy"]=[]

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_que = deque()
    search_que += graph[name]
    searched=[]
    while search_que:
        person = search_que.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+"is a mango seller")
                return True
            else:
                search_que += graph[person]
                searched.append(person)
    return False

print(search("you"))



