import sys
for i in sys.stdin:
    if i.startswith("Simon says"):
        print(i[10:])
