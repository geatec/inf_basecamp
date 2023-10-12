def check_with_lambda(lam, l):
    return filter (lam, l)

x = lambda a : a < 10
y = [1,6,19,22,7]
print(list (check_with_lambda(x, y))) #[1,6,7]

x = lambda a : a[1] == 'b'
y = ["abc", "bcd", "ube", "cur"]
print(list (check_with_lambda(x, y))) #["abc","ube"]
