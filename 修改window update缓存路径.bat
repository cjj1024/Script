net stop wuauserv
net stop bits
if exist C:\Windows\SoftwareDistribution
rmdir /S /Q C:\Windows\SoftwareDistribution
rmdir /S /Q D:\SoftwareDistribution
if not exist D:\SoftwareDistribution
mkdir D:\NewUpdateFolder
CD /D C:\Windows
mklink /J SoftwareDistribution D:\NewUpdateFolder
net start wuauserv
net start bits