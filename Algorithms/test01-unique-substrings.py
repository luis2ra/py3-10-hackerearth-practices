'''
hackerearth
link: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/unique-substrings-71b184fb/
'''

'''
Problem

You are given a string S containing only lowercase letters and an integer K. In one operation you can change any 
character of the string to '#' character.

Note: '#' is not considered when checking for duplicates.


Task

Print the minimum number of operations required such that no substring of size K contains duplicates.


Example

Assumptions

    S = "ababc"
    K = 3

Approach

- Here, in the substrings "aba" & "bab", you encounter duplicates.
- Replace the first 2 characters with '#' and the final string becomes "##abc"
- Therefore the answer is 2.


Function description

Complete the solve function provided in the editor. This function takes the following 2 parameters and returns 
an integer that represents the answer to the task as described in the problem statement:

    S: Represents the string
    K: Represents the size of the substring

Input format

Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).

- The first line contains the function parameter S.
- The second line contains the function parameter K.

Output format

Print an integer representing the answer to the given task.

Constraints

1 <= |S| <= 10^5
1 <= K <= min(|S|, 26)

Sample Input:
ababc
3

Sample Output:
2
'''
def solve (S, K):
    k = min(len(S), K)
    # print("valor de k: ", k)
    if k == len(S):
        if len(S) == len(set(S)):
            return 1
        else:
            return 0
    else:
        counter = 0
        for i in range(len(S)-k+1):
            print(S[i:i+k])

            if len(S[i:i+k]) != len(set(S[i:i+k])):
                counter += 1
        return counter

'''
Imprime el número mínimo de operaciones necesarias para que ninguna subcadena de tamaño K contenga duplicados.
'''
S = input()
K = int(input())

out_ = solve(S, K)
print (out_)
