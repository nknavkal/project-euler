def reverseIt(n):
    a = []
    b = len(str(n))
    if n%10 != 0:
        for i in range(b):
            a.append(n%10)
            n = int((n-a[-1])/10)
        a.reverse()
        for i in range(b):
            n = 10*n + a.pop()
        return n

def palindromeFinder():
    print("For this problem, we're going to find the largest palindromic number that is the product of two n-digit numbers")
    n = int(input("choose that n: "))
    allofthem = []
    for i in range (10**(2*(n-1)), 10**(2*n)):
        if i == reverseIt(i):
            allofthem.append(i)
    allofthem.reverse()
    for i in allofthem:
        for j in range(10**(n-1),10**n):
            if i%j == 0:
                if j < 1000 and j > 100 and int(i/j) < 1000 and int(i/j) > 100:
                    print(i, j, int(i/j))


palindromeFinder()
