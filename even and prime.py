#even no.s in range(0,20)
start=0
stop=21
indexing=2
for i in range(start,stop,indexing):
    print(i)


#prime no.s in range(10,50)
for num in range(10,50+1):
    if num>1:
        for y in range(2,num):
            if (num%y)==0:
                break
        else:
            print(num)


