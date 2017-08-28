# py
python scripts repository

def topNumb(listN,N=0):
    c=listN
    d=[]
    for i in c:
        if i not in d:
            d.append(i)
            
    e=[]
    for i in d:
        k=0
        for j in c:
            if i==j:
                k+=1
                
        e.append((k,i))
    
    sorted(e,reverse=True)
    e.sort(reverse=True)
    print '重复次数最多的前%d个数是：'
    if N<1:
        print e[0][1]
    else:
        for i in range(N):
            print e[i][1]
if __name__ == '__main__':
    c=[4, 10, 2, 2, 4, 9, 3, 8, 10, 10, 5, 6, 9, 7, 5, 1, 3, 6, 9, 9]
    topNumb(c,4)
