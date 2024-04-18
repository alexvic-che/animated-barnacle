states_needed = set(["mt", 'wa', 'or' , 'id' , 'nv','ut','ca','az'])
station={}

station["kone"]=set(["id", "nv", "ut"])
station["ktwo"]=set(["wa", "id", "mt"])
station["kthree"]=set(["or", "nv", "ca"])
station["kfour"]=set(["nv", "ut"])
station["kfive"]=set(["ca", "az"])

best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    if len(covered)>len(states_covered):
        best_station=station
        states_covered=covered

final_stations.add(best_station)
states_needed-=states_covered



