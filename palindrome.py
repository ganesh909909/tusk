# n=input('enter the string:')
# l=int(len(n))
# for i in range(int(l/2+1)):
#     if n[i]==n[-i-1]:
#         print('palindrome')
#         break
# else:
#     print('not')


def reverse(str1):
    if len(str1)==0:
        return(str1)
    return reverse(str1[1:])+str1[0]
a=reverse('hello')
print(a)



