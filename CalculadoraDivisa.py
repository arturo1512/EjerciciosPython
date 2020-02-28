# -*- coding: utf-8 -*-

def currency_exchance(amount):
    chilean_currency = 147.97
    return chilean_currency * amount

def change():
    print("Calculadora de divisas!")
    print('Convierte de peso Mexicano a peso Chileno')
    amount = float(input("Dame la cantidad de divisas mexicanas a cambiar:"))
    result = currency_exchance(amount)
    print('${} pasos mexicanos son ${} pesos mexicanos'.format(amount, result))

def currency_exchanceEu(peso):
    dolar_currency = 20
    return dolar_currency / peso

def changeEu():
    print("Calculadora de divisas!")
    print('Convierte de peso Mexicano a Dolares')
    peso = float(input("Dame la cantidad de divisas mexicanas a cambiar a dolares:"))
    do_result = currency_exchanceEu(peso)
    print('${} pesos mexicanos son ${} dolares'.format(peso, do_result))

def options_menu():
    print("¡Cambio de divisas!")
    print("1.- De peso mexicano a peso chileno")
    print("2.- De peso mexicano a dolares")
    option = int(input("Selecciona un tipo de cambio de divisas\n"))
    if option == 1:
        change()
    else:
        changeEu()


if __name__ == '__main__':
    options_menu()