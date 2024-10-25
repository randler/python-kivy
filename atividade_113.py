

def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    print('resultado: ', result)

print('resultado:',1*2*3*4*5*6*7*8*9*10)
multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def isPar(n):
    if n % 2 == 0:
        print('Par')
    else:
        print('Ímpar')

isPar(10)