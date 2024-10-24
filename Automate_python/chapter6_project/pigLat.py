# English to Pig Latin
print("Enter a English message to translate to Pig Latin: ")
message = input()

Vowels = ['a', 'e', 'i', 'o', 'u', 'y']

pigLatin = []
for word in message.split():
    # Separate the non-letters at the start of this word
    print(word)