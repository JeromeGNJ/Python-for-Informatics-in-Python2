t=list()
while 1:
    try:
        n = raw_input("Enter a number: ")
        if n=='done': break
        n= float(n)
        t.append(n)
    except:
        print 'Invalid Input'
        continue
    
print sum(t),len(t),sum(t)/len(t)
