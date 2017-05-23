T=int(input())
for t in range(0,T):
    a=[]
    x=[]
    
    
    for i in range(0,5):
        a.append(input().split())
    for i in range(0,5):
        a[i]=[int(i) for i in a[i]]
    a=a[0]+a[1]+a[2]+a[3]+a[4]
    x.append(input().split())
    x[0]=[int(i) for i in x[0]]
    x=x[0]
    p=0

    
        

    for k in range(0,len(x)):
        for j in range(0,25):
            if x[k]==a[j]:
                a[j]="x"
        if a[0]=="x" and a[1]=="x" and a[2]=="x" and a[3]=="x" and a[4]=="x":
            p=x.index(x[k])
            break
                

        elif a[5]=="x" and a[6]=="x" and a[7]=="x" and a[8]=="x" and a[9]=="x":
            p=x.index(x[k])
            break

        elif a[10]=="x" and a[11]=="x" and a[13]=="x" and a[14]=="x":
            p=x.index(x[k])
            break

        elif a[15]=="x" and a[16]=="x" and a[17]=="x" and a[18]=="x" and a[19]=="x":
            p=x.index(x[k])
            break

        elif a[20]=="x" and a[21]=="x" and a[22]=="x" and a[23]=="x" and a[24]=="x":
            p=x.index(x[k])
            break

        elif a[0]=="x" and a[5]=="x" and a[10]=="x" and a[15]=="x" and a[20]=="x":
            p=x.index(x[k])
            break

        elif a[1]=="x" and a[6]=="x" and a[11]=="x" and a[16]=="x" and a[21]=="x":
            p=x.index(x[k])
            break

        elif a[2]=="x" and a[7]=="x" and  a[17]=="x" and a[22]=="x":
            p=x.index(x[k])
            break

        elif a[3]=="x" and a[8]=="x" and a[13]=="x" and a[18]=="x" and a[23]=="x":
            p=x.index(x[k])
            break

        elif a[4]=="x" and a[9]=="x" and a[14]=="x" and a[19]=="x" and a[24]=="x":
            p=x.index(x[k])
            break

        elif a[0]=="x" and a[6]=="x" and a[18]=="x" and a[24]=="x":
            p=x.index(x[k])
            break

        elif a[4]=="x" and a[8]=="x"  and a[16]=="x" and a[20]=="x":
            p=x.index(x[k])
            break

        elif a[0]=="x" and a[4]=="x" and a[20]=="x" and a[24]=="x":
            p=x.index(x[k])
            break
                
            
    print(p+1)