import os,platform
os.system('git pull')
 
RAMIT=platform.architecture()[0]
if RAMIT=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif RAMIT=="64bit":
    #print('Command is in update wait we will fix it soon !')
    __import__("RAMIT")
