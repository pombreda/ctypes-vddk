Virtual Disk Development Kit from VMware makes virtual disk manipulation easy, however, C/C++ interface is not suitable for thrown-away scripting style.
ctypes-vddk acts as glue, and makes VMDK operation a lot easier.
Currently, 32bit Windows and 32bit Linux are fully supported.

Python3000 is required.
VMware Virtual Disk Development Kit is required, which can be downloaded from VMware official site.
For help on VDDK, please refer to Virtual Disk API Programming Guide.

Sample Code:
```
from VMDK import *

vddk = PyVDDK()
vddk.Create(r'test.vmdk',
	VixDiskLibCreateParams(
		VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_FLAT,
		VixDiskLibAdapterType.VIXDISKLIB_ADAPTER_SCSI_BUSLOGIC,
		VIXDISKLIB_HWVERSION_CURRENT,
		100 * 2048))
MBR = b'1' * VIXDISKLIB_SECTOR_SIZE
vddk.Open(r'test.vmdk', VIXDISKLIB_FLAG_OPEN_UNBUFFERED).Write(0, 1, MBR)
vmdk = vddk.Open(r'test.vmdk')
print('MasterBootRecord', vmdk.Read(0, 1))
print('SpaceNeededForClone', vmdk.SpaceNeededForClone())
for key in vmdk.GetMetadataKeys():
	print(key, vmdk.ReadMetadata(key))
```