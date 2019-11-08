#Simple wordlist based Hash Crack!

import os
import sys
import hashlib

print """
Author: Greg.Priest
email: papgergo89@gmail.com
"""
        
hashtype = raw_input("Hash type(md5,sha256,sha512):")
wordlist = raw_input("Wordlist name(example.txt):")
crackme = raw_input("Give me a hash:")
                     
if hashtype == "md5":
    print "in progress! Take RedBull and wait! ;]"
    with open(wordlist) as f:
        for line in f:
            for word in line.split():
                cleartext = word
                MD5 = hashlib.md5(cleartext)
                printed_MD5 = (MD5.hexdigest())
                string_MD5 = str(printed_MD5)
                file = open("MD5Hash.txt","a")
                file.write(cleartext + "\t" +string_MD5+"\n")
                file.close()
                search = open("MD5Hash.txt")
    for line2 in search:
        if crackme in line2:
            print "Hash successfully Cracked :]" 
            print line2
    print "Not found! :["
    delete_cmd = "del MD5Hash.txt"
    os.system ("echo > MD5Hash.txt")
    os.system(delete_cmd)

if hashtype == "sha256":
    print "in progress! Take RedBull and wait! ;]"
    with open(wordlist) as f:
        for line in f:
            for word in line.split():
                cleartext = word
                SHA256 = hashlib.sha256(cleartext)
                printed_SHA256 = (SHA256.hexdigest())
                string_SHA256 = str(printed_SHA256)
                file = open("SHA256Hash.txt","a")
                file.write(cleartext + "\t" +string_SHA256+"\n")
                file.close()
                search = open("SHA256Hash.txt")
    for line2 in search:
        if crackme in line2:
            print "Hash successfully Cracked :]" 
            print line2
    print "Not found! :["
    delete_cmd = "del SHA256Hash.txt"
    os.system ("echo > SHA256Hash.txt")
    os.system(delete_cmd)

if hashtype == "sha512":
    print "in progress! Take RedBull and wait! ;]"
    with open(wordlist) as f:
        for line in f:
            for word in line.split():
                cleartext = word
                SHA512 = hashlib.sha512(cleartext)
                printed_SHA512 = (SHA512.hexdigest())
                string_SHA512 = str(printed_SHA512)
                file = open("SHA512Hash.txt","a")
                file.write(cleartext + "\t" +string_SHA512+"\n")
                file.close()
                search = open("SHA512Hash.txt")
    for line2 in search:
        if crackme in line2:
            print "Hash successfully Cracked :]" 
            print line2
    print "Not found! :["
    delete_cmd = "del SHA512Hash.txt"
    os.system ("echo > SHA512Hash.txt")
    os.system(delete_cmd)
