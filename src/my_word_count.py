import sys
file=open(sys.argv[0],"r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
  print ("%s %s " %(key , wordcount[key]))
file.close();

