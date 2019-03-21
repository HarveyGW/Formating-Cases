s = input("Enter the string ")
f = input("Enter the format code (e.g. xXxxX) ")
j = 0
r=""
for i in f:
    if i == 'X':
        r+=s[j].upper()
        j+=1
    elif i == 'x':
        r+=s[j].lower()
        j+=1
    else:
        r+=i
print(r)
