class PrimeFactor:

    def of(self, number):
        factors = []
        divider = 2
        while number > 1:
            while number % divider == 0:
                factors.append(divider)
                number //= divider
            divider += 1
        return factors
