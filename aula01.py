#List comprehension - https://www.datacamp.com/tutorial/python-list-comprehension

#S = {x**2 : x in {0 ... 9}}
#V = {1, 2, 4, 8, ..., 2**12}
#M = {x | x in S and x even}

S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}
M = {0, 4, 16, 36, 64}


#l="Giovana Batista"
#k=l.split("")
#print(k)

c="".join([x.upper() for x in "Giovanna"])
print (c)

l=[x**2 for x in range(10)]
l1=sorted(l)
l2=sorted(l,reverse=True)
print (l)

d={1:'z', 3:'k', 2:'c', 5:'r'}
d2=sorted(d.items())
print (d2)
