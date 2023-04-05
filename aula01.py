#AULA 01
#List comprehension - https://www.datacamp.com/tutorial/python-list-comprehension

#S = {x**2 : x in {0 ... 9}}
#V = {1, 2, 4, 8, ..., 2**12}
#M = {x | x in S and x even}

from re import T


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

#AULA 02
#Função LAMBDA

#função aplicada
def f1(x):
    return -x
k=[2,4,8,3,6,9,5]
print (sorted(k,key=f1))
#Lambda aplica a função
print (sorted(k,key=lambda x:-x))

a = [(2,5,8),(7,1,1),(4,3,3)]
print (sorted(a,key=lambda x: sum(x)))

#Ex:
print ([x**2 for x in l])

#Ex:
m=[2,4,8,3,6,9,5]
m2=map(lambda x: x**2, m)
print (m2)

#Ex:
j=[5,8,9,8,7]
s=set(j)
print (s)

#Ex:
p=[3,2,5,8,10,15,16,18]
t=list(filter(lambda x: x%2==1, p))
print (t)

#Ex:
o = [('Fatima','G',5123),('Robson','G',1347),('Golcalves','F',5352),('Stiverson','S',4283)]
o2 = list(filter(lambda x: x[1]=='G', o))
print (max(o2))
o3=sorted(o2, key=lambda x: x[2], reverse=True)
print (o3)
o4=[x[0] for x in o3]
print (o4)
