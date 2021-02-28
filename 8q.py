l1 = []
for i in range(8):
    l1.append(list(input()))

rows = [0]*8
cs = [0]*8
diaglr = [0]*15
diagrl = [0]*15
stars = 0
    
works = True
for k in range(8):
    for l in range(8):
        if(l1[l][k]=='*'):
            stars = stars + 1
            if(rows[k] != 0):
                print("invalid")
                works = False
            elif(cs[l] != 0):
                print("invalid")
                works = False
            elif(diaglr[k-l+7] != 0):
                print("invalid")
                works = False
            elif(diagrl[k+l] != 0):
                print("invalid")
                works = False
            else :
                rows[k] += 1
                cs[l] += 1
                diaglr[k-l+7] += 1
                diagrl[k+l] += 1   
        if not works :
            break
    if not works:
        break

if works and stars == 8:
    print("valid")

if works and stars != 8 :
    print("invalid")
     
     
