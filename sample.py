from VMDK import *

VixDiskLib_Init(VIXDISKLIB_VERSION_MAJOR, VIXDISKLIB_VERSION_MINOR, NULL, NULL, NULL, NULL)
srcConnection = PyVixDiskLib_Connect()

def callback(progress):
	print(progress)
	return True

PyVixDiskLib_Create(
	srcConnection,
	r'test.vmdk',
	VixDiskLibCreateParams(
		VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_FLAT,
		VixDiskLibAdapterType.VIXDISKLIB_ADAPTER_SCSI_BUSLOGIC,
		VIXDISKLIB_HWVERSION_CURRENT,
		100 * 2048),
	callback)

diskHandle = PyVixDiskLib_Open(srcConnection, r'test.vmdk', VIXDISKLIB_FLAG_OPEN_UNBUFFERED)
print(PyVixDiskLib_GetInfo(diskHandle))
PyVixDiskLib_Write(diskHandle, 0, 1, b'1' * VIXDISKLIB_SECTOR_SIZE)
print(repr(PyVixDiskLib_Read(diskHandle, 0, 1)))
for key in PyVixDiskLib_GetMetadataKeys(diskHandle):
	print(key, PyVixDiskLib_ReadMetadata(diskHandle, key))

VixDiskLib_Exit()
