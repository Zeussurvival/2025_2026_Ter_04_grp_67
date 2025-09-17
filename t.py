import json

# a Python object (dict):
Couteau1 = {"name":"Couteau de cuisine", 
            "name" : "weapon", 
            "lore" : "Le couteau qu'utilisait la grand-mère", 
            "damage":10}
Couteau = [Couteau1]

def rewrite_all(Couteau):
    y = json.dumps(Couteau)
    with open("Items.json","w") as f:
        f.write(y)

