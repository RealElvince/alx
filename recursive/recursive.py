# sum of first 10 numbers

def cumulative(n):

    if n == 1:
        return 1
    
    else:
       return n + cumulative(n-1)
    


sum = cumulative(1)
print(sum)