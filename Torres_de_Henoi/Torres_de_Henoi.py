def Torres_Henoi(n):
    # Se só tem um disco pra mover, é só 1 movimento e pronto.
    # Esse é o nosso "primeiro dominó" da indução.
    if(n == 1):
        return 1
    
    # A fórmula mágica: 2 vezes o que você precisou discos acimo do primeiro + 1.
    # É o jeito mais rápido de provar o 2^n - 1.
    return 2 * Torres_Henoi(n - 1) + 1
n = 64
print(f"TorresDeHenoi({n}) = ", Torres_Henoi(n))
