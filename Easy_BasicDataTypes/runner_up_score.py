n = int(5)
arr = map(int, [2,3,6,6,5])
    
new_list = [i for i in arr if i != max(arr) if i in range(-100,100)] 
runner_up = max(new_list)
print(runner_up)
