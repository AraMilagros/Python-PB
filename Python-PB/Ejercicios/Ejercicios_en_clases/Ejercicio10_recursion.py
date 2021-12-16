#Funcion factorial

def factorial(n):
    if n<=1:
        return n
    return n*factorial(n-1)

#print(factorial(50))

##funcion de fibonacci de forma recursiva

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))