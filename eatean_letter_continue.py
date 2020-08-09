# Prompt the user to enter a word
# and assign it to the userWord variable.

userWord=input("Enter a word: ")
userWord=userWord.upper()
uneateanLetter=''

for letter in userWord:
    # Complete the body of the for loop.
    if letter=='A':
        continue
    elif letter=='E':
        continue
    elif letter=='I':
        continue
    elif letter=='O':
        continue
    elif letter=='U':
        continue
    else:
        uneateanLetter=letter
        
    print(uneateanLetter)