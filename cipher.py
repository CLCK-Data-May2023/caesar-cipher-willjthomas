
#set the shift
shift = 5

#define the alphabet simply by using a string
alphabet = "abcdefghijklmnopqrstuvwxyz"

#create a shifted alphabet 
shifted = alphabet[shift:] + alphabet[:shift]

#make a translation table to map alphabet to shifted alphabet
table = str.maketrans(alphabet, shifted)

#define the sentence with user input
sentence = input("Please enter a sentence: ").lower()
encrypted = sentence.translate(table)

print("The encrypted sentence is:", encrypted)