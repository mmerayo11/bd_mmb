l1 = [1, 3, 6, 8]
l2 = [1, 4, 8, 9]

res = []
for i in l1:
    if i in l2:
        res.append(i)
print(res)