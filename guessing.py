import random

print "Hello! What's your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." %name

answer = random.randint(0,101)
tries = 0

while True:
    print "Your guess?"
    guess = raw_input("> ")
    tries += 1
    int_guess = int(guess)

    if int_guess < answer:
        print "Your guess is too low, try again."
    elif int_guess > answer: 
        print "Your guess is too high, try again." 
    else: 
        print "Well done, %s! You found my number in %d tries!" % (name, tries)