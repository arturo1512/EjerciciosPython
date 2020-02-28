
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)

def run():
    numero = int(input("Dame el un numero"))
    result = factorial(numero)
    print(result)

if __name__ == '__main__':
    run()