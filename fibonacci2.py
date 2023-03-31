def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def pertence_sequencia_fibonacci(num):
    i = 0
    fibonacci_atual = 0
    while fibonacci_atual <= num:
        fibonacci_atual = fibonacci(i)
        if fibonacci_atual == num:
            return True
        i += 1
    return False

numero = int(input("Informe um número: "))

if pertence_sequencia_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
