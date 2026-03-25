def Fatorial(n):
    # O caso base: se chegar no zero, a gente para e retorna 1.
    # É o que impede o código de rodar pra sempre e dar erro.
    if(n == 0):
        return 1
    
    # Aqui tá o segredo: n vezes o fatorial do número anterior.
    # É a tradução literal da definição matemática que a gente vê em aula.
    return n * Fatorial(n-1)

n = 10
# O \n serve só pra dar um espaço na tela do terminal e não ficar tudo grudado.
print(f"\nFatorial({n}) = ", Fatorial(n))
