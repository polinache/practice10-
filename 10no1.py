__author__ = 'student'
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
C = set()
for num in A:
    x=num
    for x in A:
        if x not in B:
            C.add(x)
print(C)