def create_pass_list(d):
    result = []

    for key in d:
        if d [key][1] == "Pass":
            result.append (key)

    return result

x = {'Math':(81,"Pass"), 'Physics':(50,"Fail"), 'Chemistry':(90,"Pass"), 'English': (42,"Fail")}
passList = create_pass_list(x)
print (passList)

