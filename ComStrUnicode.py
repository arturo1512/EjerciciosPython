
def compareString(word, word2):

    if  word == word2:
        print("las palabras son iguales")
        print('La palabra 1 es {}, la palabra 2 es {} '.format(word, word2))
        print("El tamaño de la palabra 1 es: {} y el tamaño de la palabra 2 es {}".format(len(word), len(word2)))

    else:
        print("Las palabras son diferentes")
        print('La palabra 1 es {}, la palabra 2 es {} '.format(word, word2))
        print("El tamaño de la palabra 1 es: {} y el tamaño de la palabra 2 es {}".format(len(word), len(word2)))

def run():

    print("¡Programa que compara dos palabras y determina si son iguales!")
    word = str(input("Dame la primera palabra a comparar: \n"))
    word2 = str(input("Dame la segunda palabra: \n"))

    compareString(word, word2)


if __name__ == '__main__':
    run()