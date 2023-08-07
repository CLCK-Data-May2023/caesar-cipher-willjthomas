#define the sentence with user input
sentence = input("Please enter a sentence: ")
#set the shift
shift = 5

#define the alphabet simply by using a string
alphabet = "abcdefghijklmnopqrstuvwxyz"

#create a shifted alphabet 
shifted = alphabet[shift:] + alphabet[:shift]

#make a translation table to map alphabet to shifted alphabet
table = str.maketrans(alphabet, shifted)

encrypted = sentence.translate(table)

print("The encrypted sentence is:", encrypted)