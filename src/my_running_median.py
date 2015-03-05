from numpy import median
import sys

arg=sys.argv
if len(arg)>0:
  try:
     read=open(arg[1])
     write_output=open(arg[2], "w+")
     a=[]
     for i in read:
       a.append(len(i.split()))
       write_output.write(str(median(a))+'\n')
     print "output saved in", arg[2]
  except: # catch *all* exceptions
    e = sys.exc_info()[1]
    print e
else:
   print "Please provide input and output file"

