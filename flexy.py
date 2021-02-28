w, p = map(int, input().split())
l2 = [0]
lst = [int(item) for item in input().split()]
l3 = l2+lst
l3.append(w)
l1 = []
for j in range(len(l3)):
    for i in range(j):
        l1.append(l3[j] - l3[i])
l1.sort()
l1 = list(dict.fromkeys(l1))
l1 = [i for i in l1 if i != 0]
print(*l1)
