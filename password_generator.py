#!/usr/bin/env python
import random 
import string 
print ("Welcome To Python Password Generator!!")
password_length = int(input('Enter the length of Password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits 
symbols = string.punctuation 
all = lower + upper + num + symbols 
tmp = random.sample(all,password_length)
passwd = "".join(tmp)
print (passwd)
