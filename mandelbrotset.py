import numpy
import matplotlib.pyplot as plot

class MandelbrotSet:
    def __init__(self, real_range: tuple, imag_range: tuple, iteration_lim: int, coordinate_count):
        f"""
        :param real_range: range of numbers for real part of complex numbers 
        :param imag_range: range of numbers for imaginary part of complex numbers 
        :param iteration_lim: max iteration to check whether a complex number diverges or not
        :param coordinate_count: this represents the pixel count. (coordinate_count x coordinate_count)
        """

        self.__real_range = real_range
        self.__imaginary_range = imag_range
        self.__iteration_lim = iteration_lim
        self.__coordinate_count = coordinate_count

    def __iter_formula(self, constant: complex, complex_num: complex) -> complex:
        f"""
        Formula: z(n+1) = z(n)^2 + C
        
        :param constant: value of C
        :param complex_num: value of z(n)
        :return: result of the Formula as a complex Number 
        """

        return complex_num.__pow__(2).__add__(constant)

    def __get_n(self, constant: complex, complex_num: complex):
        f"""
        n equals 255 or <255 if "complex_num" diverges before 255 iterations
        
        :param constant: represents the value of C.
        :param complex_num: input for the formula. if does not diverge.
        :return: 255 or a int where complex number diverges
        """

        for color_val in range(1, self.__iteration_lim + 2):
            if abs(complex_num) > 2:
                return color_val - 1

            elif color_val > self.__iteration_lim:
                return self.__iteration_lim

            else:
                complex_num = self.__iter_formula(constant, complex_num)


    def __compute_set(self):
        f"""
        Generates given number of complex numbers and calculate the where they all diverge(n)

        :return: value of n for all complex numbers that are generates in the function
        """
        real = numpy.linspace(self.__real_range[0], self.__real_range[1], self.__coordinate_count)
        imaginary = numpy.linspace(self.__imaginary_range[0], self.__imaginary_range[1], self.__coordinate_count)

        real_grid, imag_grid = numpy.meshgrid(real, imaginary)
        complex_numbers = real_grid + imag_grid * 1j

        color_vals = numpy.ndarray(shape=(self.__coordinate_count, self.__coordinate_count))

        for x in range(self.__coordinate_count):
            for y in range(self.__coordinate_count):
                color_vals[x][y] = self.__get_n(complex_numbers[x][y], complex_numbers[x][y])
                print(x, y)
        return color_vals

    def plot(self):
        f"""
        create a visual representation of mandelbrot set
        :return: None
        """
        plot.imshow(self.__compute_set(), extent=(self.__real_range[0], self.__real_range[1],
                                                  self.__imaginary_range[0], self.__imaginary_range[1]),
                    origin="lower", interpolation="none", cmap="BrBG")
        plot.xlabel("Real")
        plot.ylabel("Imaginary")

        plot.show()







