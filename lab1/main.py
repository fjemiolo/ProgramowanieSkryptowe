from fractions import Fraction

def sum(arg1, arg2):
    if type(arg1) == complex or type(arg2) == complex:
        return complex(arg1.real + arg2.real, arg1.imag + arg2.imag)

    if type(arg1) == type(Fraction) or type(arg2) == type(Fraction):
        return arg1 + arg2

    assert float(arg1), "It's not a number!"
    assert float(arg2), "It's not a number!"
    return float(arg1) + float(arg2)


if __name__ == "__main__":
    print(f'Suma = {sum(2, 2)}')
    print(f'__name__ = {__name__}')