"""
stringjumble.py
Author: Andy
Credit: https://www.tutorialspoint.com/python/string_split.htm

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
strin = input("Please enter a string of text (the bigger the better): ")
print ("You entered \"" + strin + "\". Now jumble it:")
strinlen=len(strin)
strinlist=list(strin)
backwards=""
strinlen = strinlen-1
while strinlen > -1:
    k = strinlist[strinlen]
    backwards = backwards + str(k)
    strinlen = strinlen-1
print(backwards)
strlist=str.split(strin)
lenstrinlist = len(strlist)
lenstrinlist+=-1
backwardswords=""
while lenstrinlist > -1:
    k = strlist[lenstrinlist]
    backwardswords = backwardswords + str(k) + " "
    lenstrinlist = lenstrinlist-1
print(backwardswords)
backwordswordeach=""
for x in strlist:
    strinleneach = len(x)
    strinlisteach = list(x)
    while strinlen > -1:
        k = strinlisteach[strinleneach]
        backwardswordeach = backwardswordeach + str(k)
        strinleneach = strinleneach-1
    print(backwardswordeach)