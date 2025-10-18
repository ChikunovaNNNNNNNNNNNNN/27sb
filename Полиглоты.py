a = []
for j in range(int(input())):
    for i in range(int(input())):
        q = input()
        a.append(q)
print(a.count(max(a)) -1)
z = max(set(a), key=a.count)
print(z)
a = " ".join(dict.fromkeys(a))
s = (len(str(a).split(' ')))
d = str(a).split(' ')
a = a.split(' ')
print(s)
for i in range(s):
    print(d[i])
