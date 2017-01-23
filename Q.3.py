#no. of words in a string
str=  "many more happy returns of the day"
print('no. of words',':', len(str.split()))

#no. of letters in each word
i=0
while i<=len(str.split())-1:
    print('no. of letters in',str.split()[i],':',len(str.split()[i]))
    i += 1

