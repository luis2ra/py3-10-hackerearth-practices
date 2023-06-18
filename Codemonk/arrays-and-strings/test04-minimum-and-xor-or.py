'''
hackerearth
link: https://www.hackerearth.com/practice/codemonk/?utm_source=product&utm_medium=email&utm_campaign=welcome-email

solution explained: 
https://www.youtube.com/watch?v=jmD5V4yRMsw&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=46&ab_channel=HackerEarth
'''

'''
Minimum AND xor OR

Given an array A of N integers. Find out the minimum value of the following expression for all valid i,j.

(Ai and Aj) xor (Ai or Aj), where i != j.

Input format

- First line: A single integer T denoting the number of test cases
- For each test case:
    * First line contains a single integer N, denoting the size of the array.
    * Second line contains N space separated integers A1, A2, ..., An

Output format

For each test case, print a single line containing one integer that represents the minimum value of the given expression

Constraints
1 <= T <= 10^3
1 <= N <= 10^5
0 <= Ai <= 10^9

Note: Sum of N overall test cases does not exceed 10^6

Sample Input:
2
5
1 2 3 4 5
3
2 4 7

Sample Output:
1
3
'''

t = int(input())
results = []
while t != 0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min = arr[0] ^ arr[1]
    for i in range(1, n-1):
        temp = arr[i] ^ arr[i+1]
        if temp < min:
            min = temp
    results.append(min)
    t -= 1
for solution in results:
    print(solution)
