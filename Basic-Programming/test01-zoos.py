'''
hackerearth
link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

'''

'''
Problem

You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. 
The input word is considered similar to word "zoo" if 2 * x = y.

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such 
as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be 20.

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.
'''

word = input()
word_lower = word.lower()
z = 0
o = 0
for letter in range(len(word)):
    if word_lower[letter] == "z":
        z += 1
    elif word_lower[letter] == "o":
        o += 1
    else:
        print("No")
        break
if 2 * z == o:
    print("Yes")
else:
    print("No")
