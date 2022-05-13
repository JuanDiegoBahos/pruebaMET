class Expresion:

    def operation(self, cadena):
        """
        Permite saber si una cadena de String es, o no, una operacion aritmetica.

        :param cadena:
        :return:
        """
        try:
            # Evalua la cadena si es posible realizar una operacion aritmetica returna True.
            eval(cadena)
            it_is = True
        except Exception:
            # Si no es posible retorna False.
            it_is = False

        return it_is

    def compute(self, cadena):
        """
        Permite saber el valor de una operacion aritmetica en un String.

        :param cadena:
        :return:
        """
        if self.operation(cadena):
            # Si se puede evaluar la cadena retorna el resultado de la operacion.
            return eval(cadena)
        return False





