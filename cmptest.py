a = [(1,1),(2,4),(1,2),(2,89),(1,3),(2,48),(4,8),(5,1)]
b = []

a.sort()
print(a)

for i in range(len(a)):
    if b.count(a[i][0]) == 0:
        print(b.count(a[i][0]))
        b.append(a[i][1])

print(b)