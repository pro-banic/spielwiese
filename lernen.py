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

weiter hier:
https://youtu.be/8DvywoWv6fI?t=18979

