'''
hackerearth
link: https://www.hackerearth.com/practice/codemonk/?utm_source=product&utm_medium=email&utm_campaign=welcome-email

solution explained: 
https://www.youtube.com/watch?v=HFGZ1-y-1No&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=47&ab_channel=HackerEarth
'''

'''
The Unlucky 13

Write a program to calculate the total number of strings that are made of exactly N characters.
None of the strings can have "13" as a substring.
The strings may contain any integer from 0 - 9, repeated any number of times.

Input Format

First line: T, the number of test cases.
Next T lines: Each contain an integer N.

Output Format

Print the result of each query .
Answer for each test case should come in a new line.

Constraints

1 <= T <= 100000
0 <= N <= 1000000009

Sample Input:
2
2
1

Sample Output:
99
10
'''
cache = {}
mod = 1000000009
def ans(n):
    if n < 50000000:
        if n in cache:
            return cache[n]
        
        if n == 0:
            cache[n] = 1
            return cache[n]
        
        if n == 1:
            cache[n] = 10
            return cache[n]
        
        x = ans(n//2)
        y = ans(n//2-1)

        if (n % 2) == 0:
            cache[n] = (x*x - y*y) % mod
        else:
            z = ans(n//2 + 1)
            cache[n] = (x * (z - y)) % mod
        
        return cache[n]
    else:
        if n in cache2:
            return cache2[n]
        
        temp1 = ans(n // 2)
        temp2 = ans(n // 2 - 1)

        if (n % 2) == 0:
            cache2[n] = (temp1 * temp1 - temp2 * temp2) % mod
        else:
            temp3 = ans(n // 2 + 1)
            cache2[n] = (temp1 * (temp3 - temp2)) % mod
        
        return cache2[n]
    

inp_len = int(input())
for i in range(inp_len):
    n = int(input())

    cache2 = {}
    print(ans(n))
