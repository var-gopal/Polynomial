class Polynomial:  # defining a class ot create polynomial objects
    # defining the __init__ method to assign the coefficients to the polynomial
    def __init__(self, coefficients):
        self.coefficients = coefficients  # assigning coefficients

    def order(self):  # method to return order of the polynomial object
        # loop to find the highest power of x with non-zero coefficient
        for i in range(-1, -1 - len(self.coefficients), -1):
            if self.coefficients[i] != 0:
                return len(self.coefficients) + i

    def add(self, poly_2):  # method to add two polynomial objects
        temp_coefficients = self.coefficients.copy()  # temporary list of coefficients
        # difference in  length of lists
        diff = len(temp_coefficients) - len(poly_2.coefficients)

        if diff > 0:  # if-else statements to make list lengths the same
            for i in range(diff):
                poly_2.coefficients.append(0)
        elif diff < 0:
            for i in range(0 - diff):
                temp_coefficients.append(0)

        # creating coefficient list for the summed polynomial object
        new_coefficients = [temp_coefficients[i] + poly_2.coefficients[i]
                            for i in range(len(temp_coefficients))]

        # returning summed polynomial object
        return Polynomial(new_coefficients)

    def derivative(self):  # method to return derivative of polynomial object
        new_coefficients = self.coefficients.copy()

        # loop to populate new coefficient list with derivative coefficients
        for i in range(len(self.coefficients)):
            new_coefficients[i] = i * self.coefficients[i]

        # shifting coefficients in new list by one index to correspond to the correct powers
        new_coefficients.pop(0)

        # returning derivative polynomial object
        return Polynomial(new_coefficients)

    # method to return antiderivative of polynomial object
    def antiderivative(self, constant):
        new_coefficients = self.coefficients.copy()

        # loop to populate new coefficient list with antiderivative coefficients
        for i in range(len(self.coefficients)):
            new_coefficients[i] = self.coefficients[i] / (i + 1)

        # adding value of arbitrary constant to coefficient list
        new_coefficients.insert(0, constant)

        # returning antiderivative polynomial object
        return Polynomial(new_coefficients)

    def represent(self):  # method to return string form of a given polynomial object
        output = "P(x) = "

        # loop to concatenate terms from the coefficient list together in a string
        for i in range(len(self.coefficients)):
            if i == 0 and self.coefficients[i] != 0:
                output += str(self.coefficients[i]) + " + "
            else:
                if self.coefficients[i] != 0:
                    output += "(" + \
                        str(self.coefficients[i]) + " * x^" + str(i) + ") + "

        # returning string representation without unnecessary plus sign at end
        return output[:len(output) - 2]


def main():  # defining main method to create polynomial objects, call functions, and output required data
    p_a = Polynomial([2, 0, 4, -1, 0, 6])  # creating polynomial A
    p_b = Polynomial([-1, -3, 0, 4.5])  # creating polynomial B

    # printing order of polynomial A
    print("Order of P_a: " + str(p_a.order()))
    print()
    # printing sum of polynomials A and B
    print("P_a + P_b: " + (p_a.add(p_b)).represent())
    print()
    # printing derivative of polynomial A
    print("Derivative of P_a: " + (p_a.derivative()).represent())
    print()
    # printing antiderivative of above derivative (with provided constant term)
    print("Antiderivative of result: " +
          ((p_a.derivative()).antiderivative(2)).represent())


main()
