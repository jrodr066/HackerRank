'''
    Task:
    The provided code stub reads two integers, "a" and "b", from STDIN.

    Add logic to print two lines. The first line should contain the 
    result of integer division,  // . The second line should contain the 
    result of float division,  / .

    No rounding or formatting is necessary.
    
    a: takes in an int
    b: takes in an int
    '''
a = int(3)
b = int(5)
float_div = a//b 
int_div = a/b
print(float_div)
print(int_div)
