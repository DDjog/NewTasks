import math
import cmath
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta_calculation(self):
        """
        Calculate delta

        Parameters
        ----------
        a: real
           the coefficient of x^2
        b: real
           the coefficient of x
        c: real
           the constant

        Returns
        -------
        delta: real
               the discriminant

        Examples
        --------
        Calculate delta
        rslt=delta_calculation(2,7,5)
        print(rslt)
        9
        """
        delta = self.b * self.b - 4.0 * self.a * self.c
        return delta

    def solutions_calculation(self):
        """
        Calculate x values

        Parameters
        ----------
        a: real
           the coefficient of x^2
        b: real
           the coefficient of x
        delta: real
           the discriminant

        Returns
        -------
        x1: real
            x1 value
        x2: real
            x2 value

        Examples
        --------
        Calculate x1 and x2 values for discriminant > 0
        rslt=x_calculation(2,7,9)
        print(rslt)
        (-2.5, -2)
        """
        delta = self.delta_calculation()
        if delta > 0:
            sqrt_delta = math.sqrt(delta)
            x_one = (-self.b - sqrt_delta) / (2 * self.a)
            x_two = (-self.b + sqrt_delta) / (2 * self.a)
            return x_one, x_two

        elif delta == 0:
            x_one = -self.b / (2 * self.a)
            return x_one, x_one

        elif delta < 0:
            sqrt_delta_i = cmath.sqrt(delta)
            x_one = (-self.b - sqrt_delta_i) / (2 * self.a)
            x_two = (-self.b + sqrt_delta_i) / (2 * self.a)
            return x_one, x_two

    def __add__(self, other):
        """
                Calculate quadratic equation plus another quadratic equation

                Returns
                -------
                QuadraticEquation
                   quadratic equation as a result of two quadratic equations added

                Examples
                --------
                Added the coefficients of two different quadratic equations
                qe_another = QuadraticEquation(1, 9, 2)
                qeR = qe.add()
                print("The result of two quadratic equations added to each other is: {qeR.a}x^2 + {qeR.b}x + {qeR.c}")
                (5x^2 + 12x + 6 = 0)
                """

        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c

        return QuadraticEquation(a, b, c)


    def add_constant(self, constant):

        """
                        Calculate quadratic equation qeR plus constant

                        Returns
                        -------
                        QuadraticEquation
                           quadratic equation qeR with added constant to each coefficient

                        Examples
                        --------
                        Added constant to each coefficient of quadratic equation qeR
                        qeR = QuadraticEquation(1, 9, 2)
                        qeR_with_constant = qe_with_constant(8)
                        print("The quadratic equation eqR after {constant} added  is: {qeR_with_constant.a}x^2 + {qeR_with_constant.b}x + {qeR_with_constant.c} = 0")
                        (13x^2 + 20x + 14 = 0)
                        """

        a = self.a + constant
        b = self.b + constant
        c = self.c + constant

        return QuadraticEquation(a, b, c)


if __name__ == "__main__":
    try:
        qe = QuadraticEquation(4, 3, 4)
        qe_another = QuadraticEquation(1,9,2)
        constant = 8

        if qe.a != 0:
            d_c = qe.delta_calculation()
            print(f"Delta: {d_c}")
            x_one, x_two = qe.solutions_calculation()
            print(f"X values are: x1={x_one}, x2={x_two}")

            qeR = qe + qe_another
            print(f"The result of two quadratic equations added to each other is: {qeR.a}x^2 + {qeR.b}x + {qeR.c} = 0")

            qeR_with_constant = qeR.add_constant(constant)
            print(f"The quadratic equation eqR after {constant} added  is : {qeR_with_constant.a}x^2 + {qeR_with_constant.b}x + {qeR_with_constant.c} = 0")
        else:
            print("For a=0 no quadratic equation exists")
    except Exception as e:
        print("An error occurred: {e}")