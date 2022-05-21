#   ^ represents the starting of the number.
#   [1-9]{1} represents the starting digit in the pin code ranging from 1 to 9.
#   [0-9]{2} represents the next two digits in the pin code ranging from 0 to 9.
#   \\s{0, 1} represents the white space in the pin code that can occur once or never.
#   [0-9]{3} represents the last three digits in the pin code ranging from 0 to 9.
#   $ represents the ending of the number.
#     regex = "^[0-9]{1}  [0-9]{2}   \\s{0,1}  [0-9]{3}$"


import re


def is_valid_pin_code(pin_code):
    regex = "^[0-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    p = re.compile(regex)
    if pin_code == '':
        return False
    m = re.match(p, pin_code)
    if m is None:
        return False
    else:
        return True


if __name__ == "__main__":
    num1 = "132103"
    print(num1, ": ", is_valid_pin_code(num1))

    num2 = "201 305"
    print(num2, ": ", is_valid_pin_code(num2))

    num3 = "014205"
    print(num3, ": ", is_valid_pin_code(num3))

    num4 = "1473598"
    print(num4, ": ", is_valid_pin_code(num4))
