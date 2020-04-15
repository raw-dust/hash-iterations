import hashlib
import os
import getpass
import time

print("Enter input string")
m = getpass.getpass()
print("Enter iterations")
x = int(input())
while x >0:
    x-=1    
    m=hashlib.md5(m.encode()).hexdigest()    
print(m)
os.system("Echo "+m.strip()+"| clip")

time.sleep(1.5)
