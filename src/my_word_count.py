import sys
import re

arg=sys.argv
if len(arg)>0:
  try:
    file=open(arg[1],"r+")
    wordcount={}
    all_words=file.read()
    non_punctuation = re.sub('[^a-zA-Z0-9]', ' ', all_words)
    for word in non_punctuation.split():
       if word not in wordcount:
           wordcount[word] = 1
       else:
           wordcount[word] += 1
    file.close();    
    write_output=open(arg[2], "w+")
    for key in wordcount.keys():
       write_output.write("%s %s \n" %(key , wordcount[key]))
    print "output saved in", arg[2]
  except: # catch *all* exceptions
    e = sys.exc_info()[1]
    print e 
else:
   print "Please provide input and output file"
