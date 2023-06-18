'''
hackerearth
link: https://www.hackerearth.com/practice/codemonk/?utm_source=product&utm_medium=email&utm_campaign=welcome-email

solution explained: 
https://www.youtube.com/watch?v=mX38pWM--0M&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=43&ab_channel=HackerEarth
'''

'''
Monk and Rotation

Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned 
a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where 
she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new 
to the school, please help her to complete the task.


Input:

The first line will consists of one integer T denoting the number of test cases.

For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.

Output:
Print the required array.

Constraints:
1 <= T <= 20
1 <= N <= 10^5
1 <= N <= 10^6

Sample Input
1
5 2
1 2 3 4 5

Sample Output
4 5 1 2 3
'''

t = int(input())
while t != 0:
    n, k = map(int, input().split())
    print("n: ", n, ", k: ", k)
    arr = list(map(int, input().split()))
    print("arr: ", arr)
    index = n - (k % n)
    '''
    la sentencia siguiente da error para valores n y k muy altos
    
    index = n - k
    '''
    print("index: ", index, " k % n: ", k % n)
    for i in range(index, n):
        print(arr[i], end=" ")
    for i in range(index):
        print(arr[i], end=" ")
    print()
    t -= 1
