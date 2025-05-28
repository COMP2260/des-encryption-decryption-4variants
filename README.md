1. Bit Manipulation Utilities -- DONE

- str_to_bits(a,b) -- done
- bits_to_str(s) -- done
- hex_to_bit -- done
- bits_to_hex -- done
- xor(a,b) -> string -- done
- permute(list, table) -> string -- done

2. Key Schedule Functions -- DONE

- apply_pc1 -- done
- split_key -- done
- shift_left(bits, n ) -> shifted bits -- done
- apply_pc2 -- done

3. DES Components -- DONE

- Initial Permutation -- done
- Inverse IP -- done
- Expansion E (32-48bit) -- done
- PC1 -- done
- PC2 -- done
- S-boxes -- done
- Permutation P -- done
- Generate round key -- done

4. Implement DES Components -- DONE

- initial_permutation(block) -- done
- expansion_permutation -- done
- inverse_expansion -- done
- apply_sboxes() -- done
- permutation_p -- done
- inverse_initial_permutation -- done

5. DES Variants

- Des0 -- done
- Des1 -- done
- Des2
- Des3 -- done

6. Encryption/ Decryption
- Encryption -- done
- Decryption -- done

WORK FLOW
P: 64-bit plaintext
P': differs from P by 1 bit
K: 64-bit Key
K': differs from K by one bit

STEP 1: Conver from hex/str to binary (done)
STEP 2: Initital Permutation (done)
STEP 3: Generate Round Keys
STEP 4: Perform DES Rounds
STEP 5: Apply Inverse Initial Permutation
STEP 6: Decryption
STEP 7: Avalanche Effect Analysis

DecryptEncrypt.py:
- Consider storing the plaintext after every round, so we have data for the Avalanche Analysis.
- The numbers in each row can be calculated with sum(a != b for a, b in zip(p1[i], p2[i])), where p1[i] is P, and p2[i] is P', each after round i. 

Program Instructions:
1. Insert 'e' or 'd' into the input prompt to choose Encryption or Decryption mode (each mode takes a different file input)

2. Another input prompt will allow the user to choose a .txt file as input. Simply type the name of the file (without the .txt suffix).
    a. If mode is encryption, ensure the file has exactly 4 lines, with the first 2 being 64-bit each, and the last 2 58-bit each. There will also be checks to make sure the pairs have a 1 bit difference.

    b. If mode is decryption, ensure the file has exactly 2 lines, first one being 64-bit and the other being 58-bit.

3. For decryption, input a desired DES variant ('DES0', 'DES1', 'DES2', 'DES3', or leave blank for DES0, the default variant). This will be contained in a while loop, allowing the user to try other variants. Program stops upon receiving input '0'.

