#!/bin/python

name = raw_input("What's your name bro?")
print "Nice name {name}. \n This is how to do a for loop:\n".format(**locals())

spot = 0

for char in name:
  print "Letter {spot} is {char} in {name}.\n".format(**locals())
  spot += 1

print "There are a total of {spot} letters in your name {name}".format(**locals())

print "You can also do a for loop like this:\n"

for i in range(1, 12):
  ans = i * 7
  print "{1} x 7 = {2}".format(i, ans)



