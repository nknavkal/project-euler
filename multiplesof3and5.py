def doit ():
    num = input("pick an integer greater than 0: ")
    num = int(num)
    a = 0
    for i in range (num):
        if i%3 == 0:
            a += i
        elif i%5 == 0:
            a += i
    print("The sum of all multiples of three and five that are less than " + str(num) + " is " + str(a))
doit()
