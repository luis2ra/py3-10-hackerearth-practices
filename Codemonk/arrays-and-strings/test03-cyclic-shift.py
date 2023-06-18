'''
hackerearth
link: https://www.hackerearth.com/practice/codemonk/?utm_source=product&utm_medium=email&utm_campaign=welcome-email

solution explained: 
https://www.youtube.com/watch?v=VGYOHSWJeKU&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=45&ab_channel=HackerEarth
'''

'''
Cyclic shift

A large binary number is represented by a string A of size N and comprises of 0s (cero sub S) and 
1s (1 sub S). You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:

if the string A es [A0, A1, A2, ..., AN-1] (A sub N-1), then after performing one cyclic shift, 
the string becomes [A1, A2, ..., AN-1, A0].

You performed the shift infinite number of times and each time you recorded the value of the binary number 
represented by the string. The maximum binary number formed after performing (possibly 0) the operation is B.

Your task is to determine the number of cyclic shifts that can be performed such that the value represented by 
the string A will be equal to B for the K^th (K a la th) time.

Input format

- First line: A single integer T denoting the number of test cases
- For each test case:
    * First line: Two space-separated integers N and K
    * Second line: A denoting the string

Output format

For each test case, print a single line containing one integer that represents the number of cyclic shift 
operations performed such that the value represented by string A is equal to B for K^th (K a la th) time.

Constraints
1 <= T <= 10^3
1 <= N <= 10^5
0 <= K <= 10^9
Ai = {0,1}, for each i

Note: Sum of N overall test cases does not exceed 10^5

Sample Input:
2
5 2
10101
6 2
010101

Sample Output:
9
3
'''

t = int(input())
results = []
while t != 0:
    n, k = list(map(int, input().split()))
    s = input()
    p = -1
    max = ""
    for i in range(n):
        if max < s:
            max = s
            d = i
        elif max == s:
            p = i - d
            break
        s = s[1:] + s[:1]
    if p == -1:
        # print(d+(k-1)*n)
        results.append(d + (k-1)*n)
    else:
        # print(d+(k-1)*p)
        results.append(d + (k-1)*p)
    t -= 1
for solution in results:
    print(solution)
