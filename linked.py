#! /usr/bin/python

import sys
from VMDK import *

if len(sys.argv) == 3:
	VixDiskLib_Init(VIXDISKLIB_VERSION_MAJOR, VIXDISKLIB_VERSION_MINOR, NULL, NULL, NULL, NULL)
	srcConnection = PyVixDiskLib_Connect()
	if True:
		diskHandle = PyVixDiskLib_Open(srcConnection, sys.argv[1], VIXDISKLIB_FLAG_OPEN_READ_ONLY)
		PyVixDiskLib_CreateChild(diskHandle, sys.argv[2], VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_SPARSE)
	VixDiskLib_Exit()
else:
	print('fork a linked child disk from an existing parent')
	print('usage: %s <parent VMDK> <child VMDK>'%(sys.argv[0]))
