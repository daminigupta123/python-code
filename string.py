# mystring="hello"
# print(mystring)
# mystring='''damminniii......'''
# print(mystring)
mystring='hello'
print(mystring)
#pprint 1st char
# print(mystring[0])
#print last char using negative indexing
# print(mystring[-1])
# mystring[4]='s'
# 
s1='damini'
s2='gupta'
print(s1+s2)
print(s1*3)
count=0
for t in "damini gupta":
    if t=='i':
      count+=1
    print(count,'latters found')
    #in operator to test membership
    print('i' in 'damini gupta')
    print( "DAMINI".lower())
    print( "this will split all words in a list".split())

    print(''.join({'this','will','join'}))
    #replace function
    s1="bad morning"
    s2=s1.replace("bad","good")
    print(s1)
    print(s2)