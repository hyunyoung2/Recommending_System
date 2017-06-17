# -*- coding: utf-8 -*-

"""
Created on Thu Jun 15 15:19:38 2017

@author: hyunyoung2
"""

# -- python version : 3.6 --
# for execution command
#import sys
# for replace specialchar with ""
import re
# for time measurement betweem statement below 
import time

# project : recommending system on X in A B X C D
# A B X C D : if words nearby X are A, B, C and D, what is the most possible X?  

## -- Basic function of IO --

# @ function : read files as one strig. 
# input : file path you want to read as one string
# output : a string from beginning of file to EOF 
def readFile (absPath) :
    f = open(absPath, "r")
    
    listOfStr = f.read()
    
    f.close()
    
    return listOfStr


# @ function : remove specailChar 
# input : a string including specialChar
# output : a string without specialChar
def removalOfSpecialChar (inputStr) :
    specialChar = "[!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~…]"
    
    inputStr = re.sub(specialChar, "", inputStr)
         
    return inputStr


# -- natural lanuage processing function -- 

# @ function : tokenizing words into a word and sorting 
# input : string 
# output : List of token of words
def tokenization (wordstring) :
    tempList = wordstring.split()
    tempList.sort()
    return tempList


# @ function :  how to make nGram like bigram, threegram
# input : a sorted list  
# output : nGram list sorted like bigram, threegram 
def nGram (listOfWord, n = 5) :
    newWord = [] 
    # len of List 
    lenOfList = len(listOfWord)
    flag = 0
    # this for statement is zero-based. 
    for idx, var in enumerate(listOfWord) :
        tempStr = ""
        for i in range(0,n):
            if idx + n > lenOfList :
                flag = 1
                break
            elif i == 0 : 
                tempStr += var
            elif i + idx < lenOfList :
                #print ("no addition into list")
                #print ("total : %d, current idx : %d" % (lenOfList, (i+idx)))
                tempStr += " " + listOfWord[idx+i]
        
        if flag == 1 :
            break           
        newWord.append(tempStr)

    #sorting newWord list ahead of making dictionary of wordcounting
    #newWord.sort()
    
    return newWord


# @ function : wordcounting of nGram
# input : list of nGram
# ouput : dictionary of wordcounting 
# my case is also dicionary is sorted.
def wordCounting (nGram) :
    nDic = {}
    
    for idx, var in enumerate(nGram) :
        if nDic.get(var) == None : 
            nDic[var] = 1
        else :
            nDic[var] += 1

    return nDic

# -- functions to deal with inputstring on command like A B X C D

# @ function : 'X' uppercase change to lowercase
# in spyder, I made it 
# input : input string that you want to look for including 'x' or 'X'
# output : changed string uppercase into lowercase about 'X'
def upperCaseToLowerCase (inputStr) :
    
    if "X" in inputStr :
       return inputStr.replace("X", "x")
    

# @ function : check if inputstring on command includes 'x'
# input : inputstring including 'x'
# ouput : idx of 'x', if there is not, return None object
def isIncludingX (inputStr) :
    
    if "x" in inputStr :
        print ("sfsd")
        return inputStr.index("x")
    else :
        return None

# @ function : seperate inputstring into three types
# first : A B X mode
# seconde :  X C D mode 
# third : A B X C D mode
# input : list of inputstring on command which is what user are looking for as patter like A B X C D
# ouput : list including each of those mode(first, seconde, third)
  
def seperateMode (inputStr) :
    # tempList is 2 matrixes with two Lists
    tempList = []
    tempLen = len(inputStr)
    
    xIdx = isIncludingX(inputStr)
    
    if xIdx == None :
        print ("inputString(", inputStr, ") doesn't have 'x' or 'X' ")
        return 
    
    # only A B x
    if xIdx == tempLen-1 :
        ABx = inputStr[0:xIdx+1]
        tempList.append(ABx.split())
        tempList.append(None)
        tempList.append(None)
    # only x C D 
    elif xIdx == 0 :
        xCD = inputStr[xIdx:tempLen]
        tempList.append(None)
        tempList.append(xCD.split())
        tempList.append(None)
    else :
        ABx = inputStr[0:xIdx+1]
        xCD = inputStr[xIdx:tempLen]
        tempList.append(ABx.split())
        tempList.append(xCD.split())
        tempList.append(inputStr.split())
    
    print(inputStr)
    
    for idx, var in enumerate(tempList) :
        print (var)
    
    return tempList 

# @ intial fucntion in if __name__ == "main" :
# a sequance of this program. 
def main () :
    testPath = "C:\\Users\\hyunyoung2\\corpus\\RAW2169-CORE-test.txt"
    timerStr = ["====== recommendation system starts ======\n",
                "====== readFile function is done :",
                "====== removal of specialchar function is done :",
                "====== tokenization function is done :",
                "====== nGram is done :",
                "====== wordcounting is done :"]
    
    print (timerStr[0]) # start of this program
    
          
    testInputString = "그분들의 뜻이 X 있는지 공부하고"
    print(testInputString)
    test=upperCaseToLowerCase(testInputString)
    print (test)
    
    seperateMode(test)
    
"""
    begin = time.clock()
    tempStr = readFile(testPath)
    end1 = time.clock()
    elapsedTime = end1 - begin 
    print (timerStr[1], elapsedTime, "Seconds ======\n") # end of IO of a file
    #print (tempStr)      

    tempStr1=removalOfSpecialChar(tempStr)
    end2 = time.clock()
    elapsedTime = end2 - end1 
    print (timerStr[2], elapsedTime, "Seconds ======\n") # end of removal of specialChar
    #print (tempStr1)
    

    tempStr2=tokenization(tempStr1)
    end3 = time.clock()
    elapsedTime = end3 - end2 
    print (timerStr[3], elapsedTime, "Seconds ======\n") # end of tokenization
    #print (tempStr2)  

    tempStr3=nGram(tempStr2)
    end4 = time.clock()
    elapsedTime = end4 - end3 
    print (timerStr[4], elapsedTime, "Seconds ======\n") # end of wordcouting
    #print (tempStr3)    

    tempStr4=wordCounting(tempStr3)
    end5 = time.clock()
    elapsedTime = end5 - end4 
    print (timerStr[5], elapsedTime, "Seconds ======\n") # end of wordcouting
    #print (tempStr4)  
"""
    
    
    
# @ if statement for execution of this file   
if __name__ == "__main__" : 
    # just from Unigram to fiveGram
    # idx(0) : Unigram ... idx(4) fiveGram
    
    main()
