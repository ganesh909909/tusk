# text='helloncldmcdsjnvfnvfnmvfmakldlkasklklvmflvdfmdnldfnmdmnnsdmskl'
# print(max({text[z:y] for x in range(1, len(text)) for y in range(0, x)
#      for z in range(0, y) if text[z:y] == text[z:y][::-1]},key=len))


# text='helloncldmcdsjnvfnvfnmvfmakldlkasklklvmflvdfmdnldfnmdmnnsdmskl'
# dd = {len(text[z:y]) : text[z:y] for x in range(1, len(text))for y in range(0, x) for z in range(0, y) if text[z:y] == text[z:y][::-1]}
# keys=list(dd.keys())
# keys.sort(reverse=True)
# print(dd[keys[0]])

t='forgeeksskeegfor'
p={t[z:x] for x in range(1,len(t))for y in range(0,x)for z in range(0,y)if t[z:x]==t[z:x][::-1]}
o=(list(p))
print(o)
o.sort(key=len,reverse=True)
print(o)
print(o[-1])










