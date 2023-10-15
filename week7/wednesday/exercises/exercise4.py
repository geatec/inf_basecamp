l = [(1,5,4),(1,2),(8,5,19,10)] # 10 i.s.o. 0 to avoid ascending
l.sort (reverse = True, key = lambda aTuple: aTuple [-1])
print (l)
