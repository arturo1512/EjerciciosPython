import turtle

def main ():
    window = turtle.Screen()
    arturo = turtle.Turtle()

    make_square(arturo)
    turtle.mainloop()

def make_square(arturo):
    length = int(input("Tamaño de cuadrado: "))

    for i in range(4):
        make_line_and_turn(arturo, length)


def make_line_and_turn(arturo, length):
        arturo.forward(length)
        arturo.left(90)

if __name__ == '__main__':
    main()