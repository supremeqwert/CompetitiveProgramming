import sys
a = int(input())
set = 1
while a!=0:
    print("SET", set)
    later = []
    for i in range(a):
        if i%2 == 0:
            print(input())
        else :
            later.append(input())
    for z in reversed(later):
        print(z)
    a = int(input())
    set = set+1

    
