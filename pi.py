import math

def main():
    print("This program approximates the value of pi by summing a fixed\nnumber of terms in a series.")
    print()

    n = int(input("How many terms should I use?: "))

    total = 0.0
    sgn = 1.0
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4.0/denom
        sgn = -sgn

    print("Approximation to pi is:", total)
    print("Difference from math.pi:", math.pi - total)

main()
