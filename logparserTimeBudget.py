
import re
import os
import sys



with open(sys.argv[1],'rt') as f:
  tl = "bad"
  for line in f:
    line = line.strip('\n')
    if re.match(r"Dataset",line):
      print(line)
    if re.match(r"^Time",line,re.IGNORECASE):
      tt = tl.split(" ")
      print(tt[-1])
    tl = line
  
