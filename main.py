import Uno
import Dos

if __name__ == '__main__':
    objeto_punto1 = Uno.Matriz()

    a = [1, 2]
    b = [[1, 2], [2, 4]]
    c = [[1, 2], [2, 4], [2, 4]]
    d = [[[3, 4], [6, 5]]]
    e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
    f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]

    print("Punto 1.1")
    print(objeto_punto1.dimension(a))
    print(objeto_punto1.dimension(b))
    print(objeto_punto1.dimension(c))
    print(objeto_punto1.dimension(d))
    print(objeto_punto1.dimension(e))
    print(objeto_punto1.dimension(f))
    print("")

    print("Punto 1.2")
    print(objeto_punto1.straight(a))
    print(objeto_punto1.straight(b))
    print(objeto_punto1.straight(c))
    print(objeto_punto1.straight(d))
    print(objeto_punto1.straight(e))
    print(objeto_punto1.straight(f))
    print("")

    print("Punto 1.3")
    print(objeto_punto1.compute(a))
    print(objeto_punto1.compute(b))
    print(objeto_punto1.compute(c))
    print(objeto_punto1.compute(d))
    print(objeto_punto1.compute(e))
    print(objeto_punto1.compute(f))
    print("")


    objeto_punto2 = Dos.Expresion()

    a = "Hello ! world"
    b = "2 + 10 / 2 - 20"
    c = "(2 + 10) / 2 - 20"
    d = "(2 + 10 / 2 - 20"

    print("Punto 2.1")
    print(objeto_punto2.operation(a))
    print(objeto_punto2.operation(b))
    print(objeto_punto2.operation(c))
    print(objeto_punto2.operation(d))
    print("")

    print("Punto 2.2")
    print(objeto_punto2.compute(a))
    print(objeto_punto2.compute(b))
    print(objeto_punto2.compute(c))
    print(objeto_punto2.compute(d))
    print("")