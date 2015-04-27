import wmi
import time
import socket
import win32api

def Drives():
	drives = win32api.GetLogicalDriveStrings()
	drive_list=drives.split("\000")
	del(drive_list[len(drive_list)-1])
	return drive_list

def Keyboard():
	global info
	keyboards = info.Win32_Keyboard()
	return keyboards

def Mouse():
	global info
	mouses = info.Win32_PointingDevice()
	return mouses

def USB():
	global info
	USBs = info.Win32_USBControllerDevice()
	return USBs

def alert(msg):
	global s
	s.sendall(msg)

#-----------------------------------Check for new Insertion-------------------------------#

def newly(a,b):
	for i in b:
		if i not in a:
			return i.caption

def newlyUSB(a,b):
	for i in b:
		if i not in a:
			try:
				return i.Dependent.Name
			except:
				print "USB Removed!"
				return "None"


#---------------------------------Initial Info-------------------------------------------#
info = wmi.WMI()
drives = Drives()
keyboards = Keyboard()
mouses = Mouse()
USBs = USB()

#--------------------------------Client---------------------------------------------------#
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
	print "Socket Not Created."
server = "localhost"
port = 5555
s.connect((server,port))

#--------------------------------Checking------------------------------------------------------#

while(1):
	flag=0
	#checking for added Drives
	ndrives = Drives()
	if(len(ndrives)>len(drives)):
		alert("Drive : "+newly(drives,ndrives))
	#checking for added Keyboards
	nkeyboards = Keyboard()
	if(len(nkeyboards)>len(keyboards)):
		flag=1
		alert("Keyboard: "+newly(keyboards,nkeyboards))
	#checking for added Mouses
	nmouses = Mouse()
	if(len(nmouses)>len(mouses)):
		flag=1
		alert("Mouse : "+newly(mouses,nmouses))
	#checking for added USBs
	nUSBs = USB()
	if(len(nUSBs)>len(USBs) and flag==0):
		alert("USB : "+newlyUSB(USBs,nUSBs))
	time.sleep(1.0)

#-----------------------------------------END----------------------------------------------------#