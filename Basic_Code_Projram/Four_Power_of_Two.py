import sys

def main():
    if len(sys.argv) != 2:
        print("Enter N - where 0 <= N < 31 : ")
        return

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Invalid integer.")
        return

    if N < 0 or N >= 31:
        print("N must be between 0 <= n < 31")
        return

    print(f"Powers of 2 less than or equal to 2^{N}:")
    print("i\t2^i")
    for i in range(N + 1):
        print(f"{i}\t{1 << i}")

if __name__ == "__main__":
    main()
