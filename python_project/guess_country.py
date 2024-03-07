import random

#life time
lives = 3

# guess country from

countries = ["China",
    "India",
    "US",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico",
    "Japan",
    "Ethiopia",
    "Philippines",
    "Egypt",
    "Vietnam",
    "Turkey",
    "Iran",
    "Germany",
    "Thailand",
    "UK",
    "France",
    "Italy",
    "Tanzania",
    "Myanmar",
    "Kenya",
    "Colombia",
    "Spain",
    "Uganda",
    "Argentina",
    "Algeria",
    "Sudan",
    "Ukraine",
    "Iraq",
    "Afghanistan",
    "Poland",
    "Canada",
    "Morocco"
]
secret_word = random.choice(countries)
clue = ""

for i in range(len(secret_word)):
    guess_symbol = "?"
    clue += guess_symbol 

clue = list(clue)
heart_symbol = u'\u2764'

guess_correct = False

def updata_clue(guess_letter, secret_word, club):
    index = 0
    while index < len(secret_word):
        if guess_letter == secret_word[index]:
            clue[index] = guess_letter
        index = index + 1
        
while lives > 0:
    print(clue)
    print('You have ' + heart_symbol * lives)
    guess = input("Guess letter or a whole word (Please capitalize your first letter of the word): ")
        
    if guess == secret_word:
        guess_correct = True
        break
    
    elif guess in secret_word:
        updata_clue(guess, secret_word, clue)
        print("Great! You made a correct guess!\n")
        if '?' in clue:
            continue
        else:
            guess_correct = True
            break
        
    else:
        print("Wrong guess! You lose a life\n")
        lives = lives - 1
        

if guess_correct:
    print('You win! The country is ' + secret_word)
else:
    print('You lose, the country is ' + secret_word)
