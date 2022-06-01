x = int(1)
y = int(1)
z = int(1)
n = int(2)
    
xyzn = [ [i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k !=n ]
print(xyzn)

