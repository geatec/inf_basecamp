def switch_the_values(l):
    keys = [list (aDict.keys ()) [0] for aDict in l]
    values = list (reversed ([list (aDict.values ()) [0] for aDict in l]))
    return [{key: value} for key, value in zip (keys, values)]

x = [{'Math':81}, {'Physics':83}, {'Chemistry':87}, {'English': 42}]
print(switch_the_values(x))
#[{'Math':42, 'Physics':87, 'Chemistry':83}, {'English': 81}]

x = [{'a':'b'}, {'c':'d'}]
print(switch_the_values(x))
#[{'a':'d'}, {'c':'b'}]