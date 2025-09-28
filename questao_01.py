def verificar_paridade(n):
    if n % 2 != 0:
        raise ValueError("Número ímpar — só aceita-se números pares.")
try:
    n = int(input("Digite um número inteiro: "))
    verificar_paridade(n)
except ValueError as e:
    print("Erro:", e)
except Exception:
    print("Erro: digite um número inteiro.")
else:
    print(f"O número {n} é par.")