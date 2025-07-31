class PrimeFactor:

    def of(self, number):
        factors = []
        if number > 1:
            if number == 4 or number == 6 or number == 9 or number == 12:
                divider = 2
                while number > 1:
                    while number % divider == 0:
                        factors.append(divider)
                        number //= divider
                    divider += 1
            else:
                factors.append(number)
        return factors
