
def merge_lists_into_dictionary (l1, l2):
    return {key: value for key, value in zip (keys, values)}

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
result = merge_lists_into_dictionary(keys, values)
print(result) #{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}