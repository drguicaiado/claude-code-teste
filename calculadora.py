def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


if __name__ == "__main__":
    print("Calculadora simples")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"10 - 4 = {subtrair(10, 4)}")
    print(f"5 * 6 = {multiplicar(5, 6)}")
    print(f"15 / 3 = {dividir(15, 3)}")
