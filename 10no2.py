__author__ = 'student'
A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
X=C.difference(D)
E=X.difference(B)
print(E)