"""A script to calculate the rms (root, mean, square) of a peak voltage."""

from math import sqrt

# ask the user for the peak voltage:
print()
p_voltg = input("Enter the peak voltage: ")

rms = int(p_voltg) * (1/sqrt(2))

print("The rms of {0:}v is {1:1.3f} volts".format(p_voltg, rms))
print()
