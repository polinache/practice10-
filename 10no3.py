__author__ = 'student'
stats={}
input = open('input.txt', 'r')
words=open('input.txt', 'r').read().split()

for word in words:
    if word in stats:
        stats[word]+=1
    else:
        stats[word] =1
