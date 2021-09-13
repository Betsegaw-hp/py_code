def square(n):
    lists = {}
    c = 0
    for i in range(1,n+1):
        c += 1
        lists.update({c: (c*c)})
    return lists

result = square(5)
print(result)