from numpy import median
f=open("text")
a=[]
for i in f:
  a.append(len(i.split()))
  print median(a)

