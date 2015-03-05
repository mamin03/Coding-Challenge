import sys
import re

arg=sys.argv
if len(arg)>2:   # check if the input and out files provided
  try:
    file=open(arg[1]) # open the input file for reading
    wordcount={}      # dictionary that carries the words count
    all_words=file.read() # read the file and load it in a string
    non_punctuation = re.sub('[^a-zA-Z0-9]', ' ', all_words) # remove punctuations
    for word in non_punctuation.split(): # loop over all words
       if word not in wordcount: # if the word does not exist
           wordcount[word] = 1   # add a new key and initialize the value to 1
       else:                     # if the word exists
           wordcount[word] += 1  # update the value
    file.close();                # close the file
    write_output=open(arg[2], "w+") # open the output file for writing
    for key in wordcount.keys(): # write the output 
       write_output.write("%s %s \n" %(key , wordcount[key]))
    print "output saved in", arg[2]
  except: # catch *all* exceptions
    e = sys.exc_info()[1]
    print e 
else:
   print "Please provide input and output file"
