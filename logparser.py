
import re
import os
import sys



with open(sys.argv[1],'rt') as f:
  tl = "bad"
  for line in f:
    if re.match(r"Dataset",line):
      print(line,end='\0')
    if re.match(r"^Traceback",line,re.IGNORECASE):
      mo=re.match(r"^[0-9]*$",tl)
      if mo is not None and mo.group(0) != '':
        print(int(mo.group(0)),end='\n')
    tl = line
  
