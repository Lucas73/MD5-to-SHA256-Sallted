#encoding: utf-8
import requests
import os
import hashlib
import bcrypt
from secrets import *

hashList = []
clearHashList = []

with open('PASSWORDS.md','r') as hash:
    for element in hash:
        hashList.append(element.rstrip())

plain = open("plain.txt","w") 
for element in hashList:
  url = 'https://md5decrypt.net/en/Api/api.php'
  params = {'hash': element, 'hash_type': 'md5', 'email': emailApi, 'code': secret} 
  # add email and code from register instead emailApi and secret
  # añada el email y el código de su regirto en lugar de emailApi y de secret
  x = requests.post(url, data = params)
  clearHashList.append(x.content)
  if x.content == "":
    plain.write((" " + "\n"))
    print('Elemento guardado --> ' + x.content + "\n")
  else:
    plain.write(x.content)
    print('Elemento guardado --> ' + x.content)

plain.close() 


new_passwords = open("new_passwords.txt","w") 
outputSalts = open("outputSalts.txt","w") 
for element in clearHashList:
    salt = bcrypt.gensalt(12)
    hashedSha = hashlib.sha512(element.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if element == "":
        new_passwords.write(" " + "\n")
        outputSalts.write(" " + "\n")
    else:
        new_passwords.write(hashedSha + "\n")
        outputSalts.write(salt + "\n")
new_passwords.close()
outputSalts.close()


