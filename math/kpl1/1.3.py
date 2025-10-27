import numpy

A = numpy.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])


print(f'{"Degrees":<15} {"Radians":<15}')
for n in A:
    rad = numpy.deg2rad(n)
    print(f'{n:<15} {rad:<15.2f}')

