def create_pass_list(d):
    result = []

    for key in d:
        if d [key][1] == "Pass":
            result.append (key)

    return result

def create_fail_list(d):
    result = []

    for key in d:
        if d [key][1] == "Fail":
            result.append (key)

    return result

x = {'Soccer':(9, "Pass"), 'Snowboarding':(3, "Fail"), 'Tennis':(7, "Pass")}
passList = create_pass_list(x)
failList = create_fail_list(x)
aDict = {'Pass': passList, 'Fail': failList}

result = {}

for key in aDict:
    for element in aDict [key]:
        result [element] = key

print (result)
