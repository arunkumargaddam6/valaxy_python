i = 1

while i <= 10:
    print(i)
    i = i + 1
    # i += 1
print ("done with the loop")

################################

secret_word = "key"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
     guess = input ("enter guess: ")
     guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print ("out of guessess so you are lost")
else:
    print("you win!")


