#Nathan Luevano
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program


print("the name of the file is: " + sys.argv[0])
print("the name of the word file is: " + sys.argv[1])
print("the name of the file to be created is: " + sys.argv[2])
raw_input("Press<enter>")


#ensure format recieves 2 text files
if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

fileName = sys.argv[1]

#check if path exists
if not os.path.exists("wordCountT.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()

words = {}

#open file to count words
with open(fileName,"r") as inputFile:
    for line in inputFile:
        wordList = re.split(r'\W+',line)
        for  word  in  wordList:
            word =  word.lower()

            if word not  in words.keys():
                 words[word] = 1

            else:
                words[word] += 1

del words[""]
inputFile.close()

#Write new file with word count
with open(sys.argv[2],'w') as outputFile:
    for x ,y in sorted(words.items()): 
        outputFile.write( "%s %d\n" % (x , y) )
outputFile.close()
print("file created")

    

            
