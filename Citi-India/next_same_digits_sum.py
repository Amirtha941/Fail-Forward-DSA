
def next_same_digit_sum(N):
    target_sum=sum(map(int,str(N)))
    m=N+1
    while(True):
        if sum(map(int,str(m)))==target_sum:
            return m
        m+=1
    

N=int(input("Enter Number: "))    
result=next_same_digit_sum(N)
print(result)