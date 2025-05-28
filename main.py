import time
from DES_IMPLEMENTATION import *
from Bit_manipulation import *
from Key_Schedule import *
from DecryptEncrypt import *

if __name__ == '__main__':


    # Read input from a file
    # Assuming the file contains:
    # 2 rows of 64-bit binary strings (representing P and P') followed by
    # 2 rows of 58-bit binary strings (representing K and K')
    file = open("test_input.txt", "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()

    # Handle input validation
    if len(lines) != 4:
        raise ValueError("Input file must contain exactly 4 lines")
    if len(lines[0]) != 64 or len(lines[1]) != 64:
        raise ValueError("First two lines must be 64-bit binary strings")
    if len(lines[2]) != 58 or len(lines[3]) != 58:
        raise ValueError("Last two lines must be 58-bit binary strings")
    
    # NOTE TO NAM: *OPTIONAL*
    # Confirming P and P' are only 1 bit different
    if sum(a != b for a, b in zip(lines[0], lines[1])) != 1:
        raise ValueError("P and P' must differ by exactly one bit")
    
    # Confirming K and K' are only 1 bit different
    if sum(a != b for a, b in zip(lines[2], lines[3])) != 1:
        raise ValueError("K and K' must differ by exactly one bit")
    
    # Setting up encryption and decryption parameters
    modes = ['DES0', 'DES1', 'DES2', 'DES3']


    # Drafting output
    output = "Avalanche Demonstration\n"
    output += "P: " + lines[0] + "\n"
    output += "P': " + lines[1] + "\n"
    output += "K: " + lines[2] + "\n"
    output += "K': " + lines[3] + "\n"
    output += "Total running time: \n"
