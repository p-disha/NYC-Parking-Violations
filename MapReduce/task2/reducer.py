
#!/usr/bin/env python                                                          
import sys

count = 0
curr = 0

for line in sys.stdin:
    line = line.strip()
    
    # Fetch key-value pairs
    key, val = line.split('\t', 1)
    val = int(val)
    key = int(key)
    if(curr == key):
        count = count + val
    else:
        if count:
            print('{0:s}\t{1:s}'.format(str(curr), str(count)))
        curr = key
        count = val
if count:
    print('{0:s}\t{1:s}'.format(str(curr), str(count)))