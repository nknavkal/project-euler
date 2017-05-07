def makeTheSequence():
    print("For this problem, we're going to find the sum of all the even Fibonacci numbers below a certain number.")
    num = input("Choose that integer, and make sure it's positive: ")
    num = int(num)
    fibList = [1, 1]
    num1 = 1
    num2 = 1
    while num1 + num2 < num:
        fibList.append(num1 + num2)
        num1, num2 = num2, num1 + num2
    return fibList

def okNowSumTheEvens():
    fibList = makeTheSequence()
    a = 0
    for i in fibList:
        if i%2 == 0:
            a += i
    print(a)

okNowSumTheEvens()
