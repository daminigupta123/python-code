emptylist=[]  #ye khali rhegi 
lst=['one','two','three'] #list of strings
lst2=[1,2,3,4,5] #list of integers
lst3=[[1,2],[3,4],[5,6]] #list of lists
lst4=['one',2,[3,4],5.6] #list of mixed data types
print(emptylist)
print(lst)
print(lst2)
print(lst3)
print(lst4)
print(len(lst3)) #length of list
lst.append('four') #adding element at the end
print(lst)
lst.insert(1,'one and half') #adding element at specific index
print(lst)