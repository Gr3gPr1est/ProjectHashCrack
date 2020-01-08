#Wordlist generator!

import io
import hashlib
import sys
from itertools import product

def randString(istr):
    l = [(c, c.upper()) if not c.isdigit() else (c,) for c in istr.lower()]
    return ["".join(item) for item in product(*l)]

with open("list.txt") as f:
    for line in f:
        for word in line.split():
            cleartext = word

            variation = randString(word)
            
            for x in range(len(variation)): 
  #              print variation[x]+"\n"
                variation1 = variation[x]
                file = open("NewWordlist.txt","a")
                file.write(variation1 + "\n")
                file.close()
                print "in progress!"
print "Successfully Completed!"

