import random

print "Hello! What's your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." %name
game_in_progress = True
answer = random.randint(0,101)
tries = 0

#while not (game_in_progress):
 #   answer = random.randint(0,101)
  #  tries = 0
   # game_in_progress = True

while game_in_progress:
    print "Your guess?"
    guess = raw_input("> ")
    tries += 1
    int_guess = int(guess)
    print "answer", answer

    if int_guess < answer:
        print "Your guess is too low, try again."
    elif int_guess > answer: 
        print "Your guess is too high, try again." 
    else: 
        print "Well done, %s! You found my number in %d tries!" % (name, tries) 
        game_in_progress = False