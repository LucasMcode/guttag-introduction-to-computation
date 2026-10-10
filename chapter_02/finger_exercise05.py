prime_sum = 0
for n in range(3,1000,2):
    is_prime = True
    for j in range(3,n,2):
        if n % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += n
print(prime_sum)
