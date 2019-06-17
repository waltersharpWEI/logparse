
import re
import os
import sys

with open("../a.log",'rt') as f:
  tl = "bad"
  for line in f:
    if re.match(r"Dataset",line):
      print(line)
    if re.match(r"Trace",line):
      print(tl)
    tl = line
  
