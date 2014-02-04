import random

print "Hello! What's your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." %name

answer = random.randint(0,101)

print answer

while True:
    print "Your guess?"
    guess = raw_input("> ")
