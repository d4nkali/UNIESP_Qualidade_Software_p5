def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtracao(a, b):
    """Retorna a subtração de a por b."""
    return a - b


def multiplicacao(a, b):
    """Retorna a multiplicação de a por b."""
    return a * b


def divisao(a, b):
    """Retorna a divisão de a por b. Lança erro se b == 0."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
