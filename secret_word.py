secret_word="chupacabra"

word=input("Enter a word: ")

while(word!=secret_word):
    word=input("Enter a word:")
    if word==secret_word:
        break
print("You've successfully left the loop.")