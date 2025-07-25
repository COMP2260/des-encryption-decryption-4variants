The University of Newcastle, Australia
COMP3260 (Data Security) - Assignment 2
-------------------------------------------
4-MODE DES ENCRYPTION & DECRYPTION PROGRAM

Authors:
   - Nhu Nam Do Nguyen - 3444589
   - Chi Tai Nguyen    - 3444339

Date: 30/05/2024
-------------------------------------------
DESCRIPTION

This is a Python program designed to handle DES encryption and decryption as a 2-in-1 solution.
Alongside the standard 64-bit DES algorithm, variants outlined in the Assignment Specifications
are also included and implmented in the program.
The program will run based on 2 input prompts: mode selection, and input selection.
These promps will allow the user to choose between encryption and decrpytion, and
selecting an input file to be processed by the program, respectively.
Encryption and decryption will each produce a different output format,
coupled with results from all DES variants (DES0, DES1, DES2, DES3).
-------------------------------------------------------------------------------------------------------------------------------------
STRUCTURE

This program consists of the following files:

                * PYTHON FILES *
    - main.py                   - the main file of the program
    - DecryptEncrypt.py         - top-level functions for DES encryption/decryption
    - DES_IMPLEMENTATION.py     - core functions used during the DES transformation
    - F_FUNCTION.py             - a function that directs the encryption algorithm based on different variants of DES
    - Key_Schedule.py           - core functions and utilities to generate round keys for DES encryption/decryption
    - DES_IMPLEMENTATION.py     - core functions utilised during the f-function operation
    - Bit_manipulation.py       - helpful utilities to handle bit manipulation, decimal/hexadecimal/binary encoding and decoding
    - DES_Components.py         - a collection of predefined permutation tables to be used during the encryption/decryption process
    
                * TXT FILES *
    - README.TXT                            - this file, outlining the program's design, structure and usage
    - sample.txt                            - the default input file for encryption mode
    - sample2.txt                           - another sample input file for encryption
    - sample_output.txt                     - an Avalanche Analysis report for sample.txt
    - sample2_output.txt                    - Avalance Analysis report for sample2.txt
    - decrypt_sample.txt                    - the default input file for decryption mode
    - decrypt_sample_decryption_output.txt  - decryption results for decrypt_sample.txt

-------------------------------------------------------------------------------------------------------------------------------------
PROGRAM INSTRUCTIONS

We encourage you to use a program that natively supports Python 3.x (e.g. PyCharm, Visual Studio Code).
In the IDE, make sure to select the containing folder as the working directory of the program.
Then simply run *main.py* in a dedicated terminal, as the script will prompt the user for input.

Once the program successfully starts, follow these steps:

1.  Insert 'e' or 'd' into the input prompt to choose Encryption or Decryption mode.

2.  Another input prompt will allow the user to choose a .txt file as input.
    Simply type the name of the file (without the .txt suffix).
        a. If mode is encryption, ensure the file has exactly 4 lines, with the first 2 being 64-bit each, and the last 2 58-bit each. There will also be checks to make sure the pairs have a 1 bit difference.

        b. If mode is decryption, ensure the file has exactly 2 lines, first one being 64-bit and the other being 58-bit.

3.  Upon valid file input, the program will produce a .txt file
    outlining the results of the encryption/decryption
    in the same working directory as the input file.

    Format: [input_file]_output.txt             (for encryption)
            [input_file]_decryption_output.txt  (for decryption)

Notes:
    -   This program is designed to only take .txt files as input.
        If you have data in another format, convert the file into txt before using.

    -   The program will check that the input file meets the following criteria:
        For encryption:
            * Input has exactly 4 lines
            * Each line has exactly 64 characters
            * Every line must be a binary string (though this is not enforced, the program will fail to run otherwise)
            * First 2 and last 2 lines as pairs must differ by exactly 1 bit (a manual bit flip can be done)
        
        For decrpytion:
            * Input has exactly 2 lines
            * Each line has exactly 64 characters
            * Both line must be binary strings (same case with encryption)
            * Boh lines must differ by exactly 1 bit 
    
