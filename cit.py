import json

f = open("cities.json")

data = json.load(f)

inp = input("Please input company (Linkedin/Facebook/Amazon/Microsoft/Rovio): \n")
k = {}
for city in data:
    for company in city["company"]:
        comp = company["name"]
        if k.get(comp) != None:
            if city["city"] != k[comp][-1]:
                k[comp].append(city["city"])
            else:
                continue
        else:
            k[comp] = [city["city"]]
print(" ")   
print(inp, "in ", k[inp])