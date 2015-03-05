from numpy import median
import sys

arg=sys.argv
if len(arg)>0: # check if the input and out files provided
  try:  
     read=open(arg[1]) #  open the input file for reading
     write_output=open(arg[2], "w+") # open the output file for writing
     a=[]              # Initialize an array to carry the number of words in each line 
     for i in read:    # loop over all lines
       a.append(len(i.split())) # add the number of words
       write_output.write(str(median(a))+'\n') # write the median of updated array
     print "output saved in", arg[2]
  except: # catch *all* exceptions
    e = sys.exc_info()[1]
    print e
else:
   print "Please provide input and output file"

