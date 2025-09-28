a = input("Informe um número inteiro: ")
try:
    num = int(a)
    if num == 0:
        raise ZeroDivisionError("Erro: o divisor não pode ser zero.")
    resultado = 10 / num
except ValueError:
    print("Erro: informe um número inteiro válido.")
except ZeroDivisionError as e:
    print("Erro:", e)
else:
    print(f"10 dividido por {num} = {resultado}")