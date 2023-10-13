limit = 100
#до їх розмови будь-яке x*y де 1<x<y<x+y<limit дозволено як P
PAllowed1 = {} 
for x in range(2, limit): 
    for y in range(x+1, limit-x): 
        if x*y not in PAllowed1: 
            PAllowed1[x*y] = 1 
        else:
            PAllowed1[x*y] += 1
# коли P каже "Я  не знаю", дозволені лише  P з PAllowed1[P]>1  
SNotAllowed1 = {}  
for x in range(2, limit): 
    for y in range(x+1, limit-x): 
        if  PAllowed1[x*y] == 1 :
            SNotAllowed1[x+y] = 1  
# коли S каже "Я не знаю", дозволені лише ті S, що лежать в площині SNotAllowed1
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
# дозволені лише ті P, що можуть бути поділені на два числа x,y де x+y дозволено лише в одному варіанті, тоюто PAllowed2[P]==1      
SAllowed2 = {}  
for n in range(2, limit):
    if n not in SNotAllowed1:
        for x in range(2, n//2+1):
            if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
                if n in SAllowed2:
                    SAllowed2[n] += 1
                else:
                    SAllowed2[n] = 1
# оскільки S тепер знає відповідь, то поділ може бути здійснений лише в одному варіанті - S, де SAllowed2[S]==1
for n in SAllowed2: 
    if SAllowed2[n] == 1:
        for x in range(2, n//2+1):
            if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
                print ('(S,P) = ( %d , %d ), (x,y)= ( %d , %d )' % (n, x*(n-x), x, n-x))
