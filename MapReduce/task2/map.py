

#!/usr/bin/env python

import sys

# Fetch Key - violation code per line
for line in sys.stdin:
	line = line.strip()
	s = line.split(',')
	print("{0}\t{1}".format(s[2], '1'))