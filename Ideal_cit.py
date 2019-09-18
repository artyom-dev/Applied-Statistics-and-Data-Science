"""This algorithm finds cities where located Linkedin without industry of Gas/Oil and Chemicals and with bars chain of Moto with check less than 600
"""
import json
f = open("cities.json")
data = json.load(f)
l = []
for city in data:
    for company in city["company"]:
        if company["name"] == "Linkedin" and company["industry"] != "Gas/Oil" and "Chemicals":
            for bars in city["bars"]:
                if bars["chain"] == "Moto" and bars["check"] < 600:
                    if city["city"] in l:
                        continue
                    else:
                        l.append(city["city"])
print(l)