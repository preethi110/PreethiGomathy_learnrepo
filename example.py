import json

with open('ex5.json') as file:
    ex5 = json.load(file)

new_batter = {"id": "1004", "type": "Coffee"}
donuts = ex5["menu"]["items"]
for donut in donuts:
    if donut["id"] == "0001" and donut["type"] == "donut" and donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append(new_batter)

with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=2)
