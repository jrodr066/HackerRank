'''
Task:
    The included code stub will read an integer, "n", from STDIN.
    Without using any string methods, try to print the following:
        123 ... "n"
    Note that "" represents the consecutive values in between.
    
Constraints:
    1 <= n <= 150
'''
n = int(5)
for i in range(1,n+1):
    print(i, end ="")

