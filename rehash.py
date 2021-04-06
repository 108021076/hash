import sys
import hashlib

msg = sys.argv[1]
passwordList = []
i = 0
with open('passwordList.txt','r') as file:
    for line in file:
        currentPlace = line[:-1]
        passwordList.append(currentPlace)
if len(sys.argv) > 1 :
    while True:
        xone = hashlib.sha256(passwordList[i].encode()).hexdigest()
        xtwo = hashlib.sha1(passwordList[i].encode()).hexdigest()
        xthree = hashlib.sha512(passwordList[i].encode()).hexdigest()
        xfour = hashlib.md5(passwordList[i].encode()).hexdigest()
        if str(msg) == xone:
            print("sha256 : " + passwordList[i])
            break
        elif str(msg) == xtwo:
            print("sha1 : " + passwordList[i])
            break
        elif str(msg) == xthree:
            print("sha512 : " + passwordList[i])
            break
        elif str(msg) == xfour:
            print("md5 : " + passwordList[i])
            break
        i+=1
