def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
        return result
    
    
    list_num = (6, 12, 15, 22)
    
    for elem in list_num:
        print(factorial(elem))
        
        