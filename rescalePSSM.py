#!/usr/bin/env python
import sys, re

fname = sys.argv[1]
f = open(fname, 'r')
content = f.read()
f.close()

start = content.find("scores {")
end = content.find("}", start)
scores = re.sub("([0-9]{2})(?=[\r\n\,])", "", content[start:end])
scores = re.sub("\ (\-)?,", " 0,", scores)

f = open(fname, 'w')
f.write(content[0:start] + scores + content[end:].replace("scalingFactor 100", "scalingFactor 1"))
f.close()
