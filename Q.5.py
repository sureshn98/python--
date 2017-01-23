#checking palindrome

str ='starfish'
i = 0
n = len(str) - 1
if (str[i]==str[n]):
    print(str,'is a palindrome')
    i += 1
    n -= 1
else:
    print(str,'is not a palindrome')


