'''
Task:
    The provided code stub reads and integer,"n", from STDIN. For all non-negative integers i<n, print "i**2" .

Constraints:
    1<= n <= 20
'''
n = int(3)
for i in range(0,21):
    if i<n:
        print(i**2) 
