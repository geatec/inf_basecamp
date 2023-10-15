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

x = {'Math':(81,"Pass"), 'Physics':(50,"Fail"), 'Chemistry':(90,"Pass"), 'English': (42,"Fail")}
passList = create_pass_list(x)
failList = create_fail_list(x)
aDict = {'Pass': passList, 'Fail': failList}

result = {}

for key in aDict:
    for element in aDict [key]:
        result [element] = key

print (result)
