def calculate_fibo(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return calculate_fibo(n-1) + calculate_fibo(n-2)
    


n = 9
fibo_list = []
for i in range(n+1):
    fibo_list.append(calculate_fibo(i))

print(fibo_list)
