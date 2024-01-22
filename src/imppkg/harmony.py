import sys

from imppkg.harmonic_mean import harmonic_mean
from termcolor import cprint


print(sys.path)

x = sys.argv[1]
y = sys.argv[2]


def main():
    mylist = [float(x), float(y)]
    cprint(harmonic_mean(mylist))


main()
