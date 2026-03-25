def Fibonacci(n):
    # Fibonacci é chato porque precisa de dois casos base. 
    # Se o índice for 0, o resultado é 0.
    if(n==0):
        return 0
    
    # Se o índice for 1, o resultado é 1. Sem esses dois, o código se perde.
    if(n==1):
        return 1
    
    # A lógica da sequência: soma o termo anterior com o retrasado.
    return Fibonacci(n-1) + Fibonacci(n-2)

n = 10
print(f"Fibonacci({n}) = ", Fibonacci(n))
