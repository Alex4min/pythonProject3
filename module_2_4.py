numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  #только простые числа
not_primes = [] #не простые числа
for i in range(len(numbers)):
    is_prime = True
    i = numbers[i]
    if i < 2:
        continue
    else:
        f = i ** (1/2)
        for j in range(2, int(f+1)):
            if (i % j) == 0:
                is_prime = False
                break
        if not (is_prime):
            not_primes.append(i)
        else:
            primes.append(i)
is_prime = True
        #i += 1
print(primes)
print(not_primes)
