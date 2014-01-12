numWords = 0
numChars = 0
numSentences = 0

with open(inputfile, 'rt') as f:
    for line in f:
        numWords += line.split() 
        numChars += len(line)
    fileData = f.read()
    numSentences = len(fileData.split('. '))

autoReadIndex = 4.71* (numChars / numWords) + (words/sentences)/2 - 21.43
