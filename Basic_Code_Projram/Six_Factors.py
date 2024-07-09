def prime_factorization(N):
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N = N // 2
    
    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N = N // i
        i += 1
    
    if N > 2:
        factors.append(N)
    
    return factors

def main():
    try:
        N = int(input("Enter a positive integer to find its prime factors: "))
        if N <= 0:
            raise ValueError("Number must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    factors = prime_factorization(N)
    
    print(f"The prime factors of {N} are: {factors}")
    

if __name__ == "__main__":
    main()
