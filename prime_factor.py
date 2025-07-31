class PrimeFactor:

    def of(self, number):
        factors = []
        if number > 1:
            divider = 2
            if number == 4:
                while number % divider == 0:
                    factors.append(divider)
                    number //= divider
            elif number == 6:
                divider = 2
                while number > 1:
                    while number % divider == 0:
                        factors.append(divider)
                        number //= divider
                    divider += 1
            else:
                factors.append(number)
        return factors
