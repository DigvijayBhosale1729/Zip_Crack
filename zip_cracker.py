import zipfile
import sys
import os

if len(sys.argv)<3:
    print("Syntax is python zip_cracker.py <zip file> <dictionary file>")
    exit(0)

dic=open(sys.argv[2],'r')
zipf=open(sys.argv[1],'r')

for line in dic.readlines():
    passwd=line.strip('\n')
    try:
        zipf.extractall(pwd=passwd)
        print("Password is -->",passwd)
        exit(0)
        #Whenever, the password is incorect, the script goes to next password
    except:
        pass
print("Password Not in the dictionary file")
