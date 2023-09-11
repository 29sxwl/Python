def check_nedostat(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
        
    if sum < n:
        print("Число є недостатнім")
    else:
        print("Число є достатнім")
