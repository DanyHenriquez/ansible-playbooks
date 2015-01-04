#!/usr/bin/python

import sys, os
for peer in sys.argv[1].split('|'):
	os.system('/usr/sbin/gluster peer probe '+peer)
