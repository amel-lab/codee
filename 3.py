a = ['3', '1', '2', 'a']
if 'a' in a:
    del a[3]
    #print (a)
    a.sort()
    print ('Output :', a)

b = ['a', '3', 'b']
del b[1]
print ('No Number Found in Parameter', b )