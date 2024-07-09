def calculate_harmonic_number(N):
    harmonic_sum = 0
    for i in range(1, N + 1):
        harmonic_sum += 1 / i
    return harmonic_sum

def main():
    try:
        N = int(input("Enter the value of N (N>0): "))
        if N <= 0:
            raise ValueError("N must be a positive integer")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    result = calculate_harmonic_number(N)
    print(f"The {N}th Harmonic Number is: {result:.2f}")

if __name__ == "__main__":
    main()
