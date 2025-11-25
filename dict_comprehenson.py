# d={'a':1,'b':2,'c':3}
# for pair in d.items():
    # print(pair )
d={'a':2,'b':2,'c':3}
d={k + 'c':v*2 for k,v in d.items() if v>2}
print(d)
