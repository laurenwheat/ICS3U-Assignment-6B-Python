#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better

import math


def surface_area_triangular_prism(b1, base2, base3, hei):

    s_a = (b1 * hei) + (b1 * base3) + (base2 * base3) + (hei * base3)

    return s_a


def main():

    while True:
        try:
            b1_input = input("Enter the length of the first base (cm): ")
            b1_int = int(b1_input)
            base2_input = input("Enter the length of the second base (cm): ")
            base2_int = int(base2_input)
            base3_input = input("Enter the legth of the third base (cm): ")
            base3_int = int(base3_input)
            hei_input = input("Enter the height (cm): ")
            hei_int = int(hei_input)
            print("")

            if b1_int > 0 and base2_int > 0 and base3_int > 0 and hei_int > 0:
                triangular_prism = surface_area_triangular_prism(
                                   b1_int, base2_int, base3_int, hei_int)
                print("The surface area is {0}cm²".format(triangular_prism))
                break
            else:
                print("Input must be a positive number!!!")
        except Exception:
            print("That is not even a number!!")
        finally:
            print("Wanna try again :)?")


if __name__ == "__main__":
    main()
