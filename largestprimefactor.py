def isPrime(n):
    sqrt = int(n**.5 // 1)
    for i in range (2, sqrt + 1):
        if n%i == 0:
            return isPrime(max(i, int(n // i)))
    return(n)


def maxFactor():
    print("For this problem, we're going to find the largest prime factor of a certain number.")
    num = input("Choose that integer, and make sure it's positive, you smarmy bastard: ")
    num = int(num)
    print(isPrime(num))
maxFactor()
