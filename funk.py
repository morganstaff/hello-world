#!/bin/python



def say_hello():
  print "Hello"

def greeting(name, what):
  print "Hello {name}!\nThis is what I'm supposed to say:\n\t{what}".format(**locals())

print "Call function hello"

say_hello()

message = raw_input("What do you want to me to say?")
name = raw_input("Who am I saying this to?")

greeting(name, message)
