x = input("ENTER STRING : ")
d = dict()

for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        
h = len(d)
for i in d:
    c=0
    d[i]-=1
    l =list(d.values())
    k=1
    while k<=len(d):
        for j in d:
            if l[k-1]==d[j] or d[j]==0 or l[k-1]==0:
                c+=1
            else:
                continue
        k+=1
        m=0
        if c==h*h:
            m+=1
            break
    d[i]+=1
    if m>0:
        break
if m>0:
    print("True")
else:
    print("False")
