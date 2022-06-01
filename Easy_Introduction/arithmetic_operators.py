'''
Task:
  The provided code stub reads two integers from STDIN, "a" and "b". Add code to print three lines where:

  1) The first line contains the sum of the two numbers.
  2) The second line contains the difference of the two numbers (first - second).
  3) The third line contains the product of the two numbers.
  
Constraints:
  a: 1<= a <= 10**10
  b: 1<= b <= 10**10
'''
a = int(5)
b = int(2)
if a>=1 or b>=1:
    print(a + b)
    print(a - b)
    print(a * b)
else:
    print("Not in range.") 
