def switching_slice(A):
    n = len(A)
    if n <= 2:
        return n
    
    cur_sum = 2
    max_sum = 2
    
    for i in range(2, n):
        if A[i] == A[i-2]:
            cur_sum += 1
        else:
            cur_sum = 2
        max_sum = max(max_sum, cur_sum)
    
    return max_sum

# Proper input handling
A = list(map(int, input("Enter elements separated by space: ").split()))
result = switching_slice(A)
print(result)
