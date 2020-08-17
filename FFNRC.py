# def firstNotRepeatingCharacter(my_string):
#     for i in range(len(my_string)):
#         isRepeating=False
#         for j in range(len(my_string)):
#             if my_string[i]==my_string[j] and i!=j:
#                 isRepeating=True
#         if not isRepeating:
#             return my_string[i]
#     return  '_'
# print(firstNotRepeatingCharacter('aabducdb'))


def func(g):
    for c in g:
        if g.index(c)==g.rindex(c):
            return(c)
    return'_'
print(func('aabbcctg'))




