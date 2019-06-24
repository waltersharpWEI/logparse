
import re
import os
import sys



with open(sys.argv[1],'rt') as f:
  tl = "bad"
  ct = 0
  timeb = 0
  for line in f:
    line = line.strip('\n')
    if re.match(r"##",line):
      print(line)
      timeb = int(line.split(" ")[-2])
    if timeb == 0:
      continue
    if re.match(r"Target accuracy",line):
      print("targetAccuracy=" + line.split(" ")[-1])
      print("timeBudget=" + str(timeb))
    if re.match(r"Dataset",line):
      print(line)
    if re.match(r"^Time",line,re.IGNORECASE):
      tt = tl.split(" ")
      print(tt[-1])
    if re.match(r"^Sigma",line):
      tt = line.split(" ")
      ct = 3
      print("sigma=" + tt[-1])
    elif ct == 3:
      if not re.match(r"^kimg",line):
        print("iter=" + line)
        ct -= 1
    elif ct == 2:
      if not re.match(r"^kimg",line):
        print("time=" + line)
        ct -= 1
    elif ct == 1:
      if not re.match(r"^kimg",line):
        print("accuracy=" + line)
        ct -= 1
    tl = line
  
