import Uno

if __name__ == '__main__':
    objeto_punto1 = Uno.Matriz()

    a = [1, 2]
    b = [[1, 2], [2, 4]]
    c = [[1, 2], [2, 4], [2, 4]]
    d = [[[3, 4], [6, 5]]]
    e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
    f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]

    print(objeto_punto1.compute(a))
    print(objeto_punto1.compute(b))
    print(objeto_punto1.compute(c))
    print(objeto_punto1.compute(d))
    print(objeto_punto1.compute(e))
    print(objeto_punto1.compute(f))