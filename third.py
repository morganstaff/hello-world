#!/bin/python

l = raw_input("Enter a letter: ")

vowels = ['a', 'e', 'i', 'o', 'u']

consenants = 'bcdfghjklmnpqrstvwxyz'

if l in vowels:
  print "{l} is a vowel".format(**locals())
elif l in consenants:
  print "{l} is a c-c-c-consenant.".format(**locals())
else:
  print "{l} is nothing!".format(**locals())