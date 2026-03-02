def calculate_fibo(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return calculate_fibo(n-1) + calculate_fibo(n-2)