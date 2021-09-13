# a -b
def lineReader(n, pos = 0): 
    inputFile = open('work.txt', 'r')
    Lines = inputFile.readlines()
    count = 0

    if(pos == 1): 
        pos = len(Lines)
        if n < pos :
            count = n 
            pos,n = n, pos

    for x in range(pos, n):
        count += 1
        print("Line{}: {}".format(count, Lines[x]))

    inputFile.close()

# c
def storeLines(): 
    inputFile = open('work.txt', 'r')
    Lines = inputFile.readlines()
    # print(Lines)
        # or
    lineList = []

    for line in Lines: # to store line by line
        lineList.append(line)
    print(lineList)
    inputFile.close()

# d
def longestWordFinder(): 
    inputFile = open('work.txt', 'r')
    Lines = inputFile.readlines()
    wordList = set(())

    for line in Lines:
        wordList.update(line.split())
    for word in wordList:
        if(max(wordList) == word):
            print({word :"{} letters".format(len(word))})
        
    inputFile.close()

# e
def countLine(): 
        inputFile = open('work.txt', 'r')
        Lines = inputFile.readlines()
        print("{} Lines".format(len(Lines)))
        inputFile.close()

# f
def copyTo(fileName = 'mywords.txt'):
    if(type(fileName) != str) :
        fileName = '{}'.format(fileName) 
    # read file
    inputFile = open('work.txt', 'r')
    Lines = inputFile.readlines()

    # wirte to the given file
    createFile = open(fileName, 'w')
    createFile.writelines(Lines)

    createFile.close()
    inputFile.close()

# Uncomment the f/f to excute

# lineReader(5)     # 0 ==> read first n (default)
                    # 1 ==> read last n 
# storeLines()
# longestWordFinder()
# countLine()
# copyTo()      # takes  string file name as parameter (file extension should be inculded)      
                # 'mywords.txt' is the default if there is no params given