fname = input("Datei: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        di[w] = di.get(w,0) + 1
       # print(w, "new: ", di[w])
print(di)
largest = -1
for k,v, in di.items():
   # print (k,v)
    if v > largest:
        largest = v
        theword = k
print ("das meistgenutzte Wort ist: ", theword, largest)


'''
weiter hier:
https://youtu.be/8DvywoWv6fI?t=19410
'''



