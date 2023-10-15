def create_list_from_tuples(a):
    result = []

    for aTuple in a:
        for anItem in aTuple:
            result.append (anItem)
            
    return result

l = [(1,5,4),(1,2),(8,5,19,0)]
print(create_list_from_tuples(l))
#[1,5,4,1,2,8,5,19,0]
