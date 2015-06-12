#!/usr/bin/python
import sys
f = open('/etc/passwd')
lines = f.readlines()
highestuid = 0
highestline = ''
highuid = 0
highline = ''
nextuid = 0
nextline = ''
uid = []
intofuid = 0
counter = 0
for i in lines:
    intofuid = i.split(':')[2]
    uid.append(intofuid)
    uid.sort(key=int, reverse=True)
for u in uid:
    counter = counter + 1
    if counter == 2:
        print "All done!"
        sys.exit(0)
    for line in lines: 
        if u in line:
            print line
  
