#!/usr/bin/env python

import sys

totalWords = 0
totalChars = 0
totalSentences = 0

# take file as command-line argument
file = sys.argv[1]
with open(file) as f:
    for x in f.readlines():
        if ('.' in x or '?' in x or '!' in x):
            totalSentences += 1
        totalChars += len(x)
        totalWords += len(x.split())

autoReadIndex = 4.71* (float(totalChars) / float(totalWords)) + (float(totalWords)/float(totalSentences))/2 - 21.43 
print ("The Automated Readability Index of " + str(file) + " is " + str(autoReadIndex))
