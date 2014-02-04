import random

print "Hello! What's your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." %name
game_in_progress = True
answer = random.randint(1,100)
tries = 0

# create a string list of valid guesses
list_of_valid_int_guesses = []
n = 1
while n < 101:
    n_in_string = str(n)
    list_of_valid_int_guesses.append(n_in_string)
    n += 1

while game_in_progress:
    print "Your guess?"
    guess = raw_input("> ")
    
    # check if user input is valid
    if guess in list_of_valid_int_guesses:
        tries += 1
        int_guess = int(guess)

        if int_guess < answer:
            print "Your guess is too low, try again."
        elif int_guess > answer: 
            print "Your guess is too high, try again." 
        else: 
            print "Well done, %s! You found my number in %d tries!" % (name, tries) 
            game_in_progress = False
    else: 
        print "Please guess a number between 1 and 100."