import hashlib
import os

hash=input("enter the hash code of md5:  ")
file=input("file name :")
#print(file)
try:
    pas=open(file,"r")
    
except:
    print("no file found")
    quit()
   
for p in pas:
    enc_word=p.encode('utf-8')
    d=hashlib.md5(enc_word.strip()).hexdigest()
    
    print("please wait")
    print(d)
    print(hash)
    print(p)
    try:
        os.system("cls")
    except:
        os.system("clear")

    if(d==hash):
        print("password found:"+p)
        quit()
    
    #783ed55b5ec4de1b0386fb7b3abdba66
    #ade3ce428ebb3eb3c58a21581eca9cef
