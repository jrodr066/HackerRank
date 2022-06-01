'''
Task:
    Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a
    cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum 
    of is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
'''
x = int(1)
y = int(1)
z = int(1)
n = int(2)
    
xyzn = [ [i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k !=n ]
print(xyzn)

