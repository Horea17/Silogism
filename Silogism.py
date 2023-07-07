import re
from difflib import SequenceMatcher

p1 = input("Dati prima propozitie")
p2 = input ("Dati a doua propozitie")
a = 0
b = 0
c = 0
d = 0
a = re.search("Toti", p1) or re.search("Niciun", p1)
if a:
    c = 1
else:
    c = 3
b = re.search("nu", p1)
if b:
    c = c+1
if c ==1:
    print("p1 este universal afirmativa")
elif c == 2:
    print("p1 este universal negativa")
elif c == 3:
    print("p1 este particular afirmativa")
else:
    print("p1 este particular negativa")

d = re.search("Toti", p2) or re.search("Niciun", p2)
if d:
    e = 1
else:
    e = 3
f = re.search("nu", p2)
if f:
    e = e+1
if e ==1:
    print("p2 este universal afirmativa")
elif e == 2:
    print("p2 este universal negativa")
elif e == 3:
    print("p2 este particular afirmativa")
else:
    print("p2 este particular negativa")


def lastWord(string):
    lis = list(string.split(" "))
    length = len(lis)
    return lis[length - 1]
figura = 0
termenulmediu=""
subiect=""
predicat=""
t1= p1.split(' ')[1]
print(t1)
t2 = lastWord(p1)
print (t2)
t3= p2.split(' ')[1]
print(t3)
t4 = lastWord(p2)
print (t4)
print(SequenceMatcher(a=t2,b=t4).ratio())
prag=0
while prag==0:
    z = SequenceMatcher(a=t2,b=t4).ratio()
    y = re.search("sa", p1) or re.search("sa", p2)
    if y:
        if z>0.3:
            termenulmediu=t2
            figura=2
            subiect=t3
            predicat=t1
            prag = 1

    else:
        if z>0.8:
            termenulmediu=t2
            figura=2
            subiect = t3
            predicat = t1
            print("predicatul este", predicat, "subiectul", subiect, "termenul mediu", termenulmediu)
            prag = 1


    z = SequenceMatcher(a=t1, b=t4).ratio()
    if z > 0.8:
        termenulmediu = t1
        figura = 1
        predicat=t2
        subiect = t3
        prag = 1
        print("predicatul este", predicat, "subiectul", subiect, "termenul mediu", termenulmediu)

    z = SequenceMatcher(a=t1,b=t4).ratio()
    y =  re.search(" sa ", p2)
    if y:
        if z>0.3:
            termenulmediu=t1
            figura=1
            subiect=t3
            predicat=t2
            prag = 1

    else:
        if z>0.8:
            termenulmediu=t1
            figura=2
            subiect = t3
            predicat = t2
            print("predicatul este", predicat, "subiectul", subiect, "termenul mediu", termenulmediu)
            prag = 1

    z = SequenceMatcher(a=t2,b=t3).ratio()
    y = re.search("sa", p1) or re.search("sa", p2)
    if y:
        if z>0.3:
            termenulmediu=t2
            figura=4
            subiect=t4
            predicat=t1
            prag = 1

    else:
        if z>0.8:
            termenulmediu=t2
            figura=4
            subiect = t4
            predicat = t1
            print("predicatul este", predicat, "subiectul", subiect, "termenul mediu", termenulmediu)
            prag = 1
print (figura)
