import requests
import os
import hashlib
import bcrypt
from secrets import *

with open('PASSWORDS.md','r') as hash:
    lineas = hash.readlines()

hashList = []
clearHashList = []

for element in lineas:
    hashList.append(element.strip())

outputClearHashes = open("outputClearHashes.txt","w") 
index = 0
for element in hashList:
  url = 'https://md5decrypt.net/en/Api/api.php'
  params = {'hash': element, 'hash_type': 'md5', 'email': emailApi, 'code': secret} 
  # add email and code from register instead emailApi and secret
  # añada el email y el código de su regirto en lugar de emailApi y de secret
  x = requests.post(url, data = params)
  clearHashList.append(x.content)
  index += 1
  outputClearHashes.write(str(index) + " " + x.content + "\n") 

outputClearHashes.close() 


outputClearHashesToSHA = open("outputClearHashesToSHA.txt","w") 
outputSalts = open("outputSalts.txt","w") 
index2 = 0
for element in clearHashList:
    index2 += 1
    salt = bcrypt.gensalt(12)
    hashedSha = hashlib.sha512(element.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    outputClearHashesToSHA.write(str(index2) + " " + hashedSha + "\n")
    outputSalts.write(str(index2) + " " + salt + "\n")
outputClearHashesToSHA.close()
outputSalts.close()
