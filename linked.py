#! /usr/bin/python

import sys
import VMDK

if len(sys.argv) == 3:
	VMDK.PyVDDK().Open(sys.argv[1]).CreateChild(sys.argv[2])
else:
	print('fork a linked child disk from an existing parent')
	print('usage: %s <parent VMDK> <child VMDK>'%(sys.argv[0]))
