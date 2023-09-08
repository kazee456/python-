secret_word = "Skipper"
guess=""
guess_count=0
guess_limit=3
guess_end= False

while guess!= secret_word and not(guess_end):
    if guess_count<guess_limit:
      guess =input  ("Enter the guess: ")
      guess_count+=1
    else:
       guess_end=True 
if guess_end:
   print("You Lose!, Out of Guesses")
else:
   print("You are a genius, You Win!")