def square_generator(n):
    result = []  
    for i in range (n):
        k = (i + 1) ** 2
        result.append(k)
    return result

n = int(input("Enter a number: "))
squares = square_generator(n)
for square in squares:
    print (square)

def evens(n):
    result = []
    for i in range (n):
        if i % 2 == 0:
            result.append(i)
    return result

n = int(input("n: "))
k = evens(n)
print (k)

def d34(n):
    result = []
    for i in range (n):
        if i % 3 == 0 and i % 4 == 0:
            result.append(i)
    return result

n = int(input("n: "))
k = d34(n)
print (k)

def d34(n):
    result = []
    for i in range (n , 0 , -1):
        result.append(i)
    return result

n = int(input("n: "))
k = d34(n)
print (k)