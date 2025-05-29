import time
from DecryptEncrypt import *
from Bit_manipulation import bin2hex

if __name__ == '__main__':

    modeselect = input("Select Encryption or Decryption mode (E/D): ").strip().upper()
    while modeselect not in ['E', 'D']:
        modeselect = input("Invalid selection. Please select 'E' for Encryption or 'D' for Decryption: ").strip().upper()
    
    # Encryption mode
    if modeselect == 'E':
        # Read input from a file
        # Assuming the file contains:
        # 2 rows of 64-bit binary strings (representing P and P') followed by
        # 2 rows of 64-bit binary strings (representing K and K')
        while True:
            try:
                filename = input("Enter the input file name, do not include the '.txt' suffix (e.g.: test_input). Leave blank for default input file: ").strip() or "sample"
                file = open(filename + ".txt", "r")
                lines = []
                for line in file:
                    lines.append(line.strip())
                file.close()
                break
            except:
                print("File not found. Please ensure the file exists and try again.")

        # Handle input validation
        if len(lines) != 4:
            raise ValueError("Input file must contain exactly 4 lines")
        if len(lines[0]) != 64 or len(lines[1]) != 64 or len(lines[2]) != 64 or len(lines[3]) != 64:
            raise ValueError("All lines must be 64-bit binary strings")
        
        # Confirming P and P' are only 1 bit different
        if sum(a != b for a, b in zip(lines[0], lines[1])) != 1:
            raise ValueError("P and P' must differ by exactly one bit")
        
        # Confirming K and K' are only 1 bit different
        if sum(a != b for a, b in zip(lines[2], lines[3])) != 1:
            raise ValueError("K and K' must differ by exactly one bit")
        
        # Setting up encryption and decryption parameters
        modes = ['DES0', 'DES1', 'DES2', 'DES3']

        # Starting the timer
        start_time = time.time()
        
        # Perform encryption and analysis
        avalanche_output_same_key = analysis_table(lines[0], lines[1], lines[2], lines[3], mode='same-key')
        avalanche_output_different_key = analysis_table(lines[0], lines[1], lines[2], lines[3], mode='different-key')
        
        # Ending the timer
        end_time = time.time()
        total_time = end_time - start_time

        # Drafting output
        output = "Avalanche Demonstration\n"
        output += "Plaintext P:\t" + lines[0] + f" (H: {bin2hex(lines[0])})" + "\n"
        output += "Plaintext P':\t" + lines[1] + f" (H: {bin2hex(lines[1])})" + "\n"
        output += "Key K:\t\t\t" + lines[2] + f" (H: {bin2hex(lines[2])})" + "\n"
        output += "Key K':\t\t\t" + lines[3] + f" (H: {bin2hex(lines[3])})" + "\n"
        output += "Total running time: " + str(total_time) + " seconds\n\n"
        output += avalanche_output_same_key + "\n" + avalanche_output_different_key

        # Write output to a file
        with open(f"{filename}_output.txt", "w") as output_file:
            output_file.write(output)
        
        print(f"Analysis complete. Output written to {filename}_output.txt")
    
    # Decryption mode
    else:
        # Handling file input for decryption
        while True:
            try:
                filename = input("Enter the input file name, do not include the '.txt' suffix (e.g.: test_input). Leave blank for default input file: ").strip() or "decrypt_sample"
                file = open(filename + ".txt", "r")
                lines = []
                for line in file:
                    lines.append(line.strip())
                file.close()
                break
            except:
                print("File not found. Please ensure the file exists and try again.")

        # Handle input validation
        # Assuming the file contains exactly 2 lines of 64-bit binary strings
        # 1st line: ciphertext C
        # 2nd line: key K
        if len(lines) != 2:
            raise ValueError("Input file must contain exactly 4 lines")
        if len(lines[0]) != 64 or len(lines[1]) != 64:
            raise ValueError("Both lines must be 64-bit binary strings")
        
        # Perform decryption
        decrypted_text = decrypt(lines[0], lines[1]) # DES0

        # Drafting output
        output = "DECRYPTION\n"
        output += "Ciphertext C:\t" + lines[0] + f" (H: {bin2hex(lines[0])})" + "\n"
        output += "Key K:\t\t\t" + lines[1] + f" (H: {bin2hex(lines[1])})" +"\n"
        output += "Plaintext P:\t" + decrypted_text + f" (H: {bin2hex(decrypted_text)})"

        # Write output to a file
        with open(f"{filename}_decryption_output.txt", "w") as output_file:
            output_file.write(output)
        
        print(f"Decryption complete. Output written to {filename}_decryption_output.txt")