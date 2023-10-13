limit = 100

PAllowed1 = {} 
for x in range(2, limit): 
    for y in range(x+1, limit-x): 
        if x*y not in PAllowed1: 
            PAllowed1[x*y] = 1 
        else:
            PAllowed1[x*y] += 1

# Якщо хоч одна пара дає добуток, який з'являється в PAllowed1 хоч 1 раз, тоді ця сума додається в SNotAllowed1 "P міг би знати"
SNotAllowed1 = {}  
for x in range(2, limit): 
    for y in range(x+1, limit-x): 
        if  PAllowed1[x*y] == 1 :
            SNotAllowed1[x+y] = 1  

# S би не міг одразу визначити пару чисел з заяви P
PAllowed2 = {} 
for n in range(2, limit):
    if n not in SNotAllowed1:
        for x in range(2, n//2+1):
            p = x * (n-x)
            if p in PAllowed1 and PAllowed1[p] > 1:
                if p in PAllowed2:
                    PAllowed2[p] += 1
                else:
                    PAllowed2[p] = 1 
    
SAllowed2 = {}  
for n in range(2, limit):
    if n not in SNotAllowed1:
        for x in range(2, n//2+1):
            if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
                if n in SAllowed2:
                    SAllowed2[n] += 1
                else:
                    SAllowed2[n] = 1

print(SAllowed2)


for n in SAllowed2: 
    if SAllowed2[n] == 1:
        for x in range(2, n//2+1):
            if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
                print ('(S,P) = ( %d , %d ), (x,y)= ( %d , %d )' % (n, x*(n-x), x, n-x))