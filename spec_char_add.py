import io
import hashlib
import sys
from itertools import product

def my_function():
    a = 0
    while (a != 8):
        if (a == 0):
            char = "!"
        if (a == 1):
            char = "%"
        if (a == 2):
            char = "/"
        if (a == 3):
            char = "="
        if (a == 4):
            char = "("
        if (a == 5):
            char = ")"
        if (a == 6):
            char = "'"
        if (a == 7):
            char = '"'
        if (a == 8):
            char = "+"
        file = open("NewWordlist.txt","a")
        file.write(word + char*s+"\n")
        file.close()
        print "Successfully!"
        a = a +1
    
with open("list2.txt") as f:
    for line in f:
        for word in line.split():
            s = 0
            while (s!=10):
                my_function()
                s = s+1
                

