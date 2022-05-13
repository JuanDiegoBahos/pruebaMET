class Matriz:

    def dimension(self, lista):
        """
        Permite conocer la dimension de una matriz.

        :param lista:
        :return:
        """

        if isinstance(lista, list):
            return 1 + (max(map(self.dimension, lista)) if lista else 0)
        return 0

    def straight(self, lista):
        """
        Determina si cada lista tiene el mismo tamaño en cada una de sus profundidades
        :param lista:
        :return:
        """
        dimensiones_lista = self.ob_dimension(lista)
        if not isinstance(dimensiones_lista, list):
            return True
        return dimensiones_lista.count(dimensiones_lista[0]) == len(dimensiones_lista)

    def ob_dimension(self, lista):
        """
        Retorna una lista con los tamaños de la sublista y/o sublistas
        :param lista:
        :return:
        """
        lista_nueva = []
        for item in lista:
            if not isinstance(item, list):
                return len(lista)
            if type(item) in [list, str]:
                respuesta = self.ob_dimension(item)

                lista_nueva.append(respuesta) if isinstance(respuesta, int) else lista_nueva.extend(respuesta)

        return lista_nueva

    def compute(self, lista):
        """
        Permite saber la suma total de todos los valores dentro de una matriz.

        :param lista:
        :return:
        """
        if isinstance(lista, list):
            return 0 + (sum(map(self.compute, lista)) if lista else 0)
        return lista
