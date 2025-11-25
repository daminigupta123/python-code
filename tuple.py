#touple with mix datatype
t=(1,'raju',30,'abc')
print(t)
#neted touple
t=(1,(2,3,4),(1,'raju',2))
print(t)
t="damini",
print(type(t))
print(t)
t=('satish','murali')
print(t[1])
#nested touple
t=('satish',('raju',123))
print(t[1])
#sliciing
t=(1,2,3,4,5,5)
print(t[1:4])
#print elemnets form starting to 2nd last elements
print(t[:-2])
#print elemnets from starting to end
print(t[:])
t=(1,2,3,4,[5,6,7])
# t[2]="x"
# print(t)
t[4][1]='satish'
print(t)
t=(1,2,3,3)+(4,5,6)
# del t
t=(1,2,2,3,3,2,4,4,4)
print(max(t))
print(min(t))
print(sum(t))
new_t=sorted(t)
print(new_t)

t.count(2)
print(len(t))
print(t.count(2))
# print(t)

