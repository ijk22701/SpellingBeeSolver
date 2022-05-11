from re import search

words = []
with open('ScrabbleWordList4Char+.txt') as f:
    line = f.readline()
    for line in f:
        size = len(line)
        newLine = line[:size - 1]
        words.append(newLine)

totalWords = len(words)

mustContain = ""
otherLetters = []
mustContain = input("Enter the central letter -> ").lower()
for int in range(6):
    valid = False
    while not valid:
        newLetter = (input("Enter one of the letters -> ")).lower()
        valid = True
        for currentLetterInList in otherLetters:
            if newLetter == currentLetterInList:
                valid = False
        if valid == True:
            otherLetters.append(newLetter)
        else:
            print("Letter is already in list!")

print (otherLetters)
otherLetters.append(mustContain)

validWords = []
for word in words: 
    if search(mustContain, word) and all(x in otherLetters for x in word):
        validWords.append(word)
        


print("Valid words are: ")
for word in validWords:
    print(word)

exitKey = input ("Press any key to exit")