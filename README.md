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
- Inverse expansion -- NOT DONE
- Generate round key -- done

4. Implement DES Components

- initial_permutation(block) -- done
- expansion_permutation -- done
- inverse_expansion
- apply_sboxes() -- done
- permutation_p -- done
- inverse_initial_permutation -- done

5. DES Variants

- Des0 -- done
- Des1 -- done
- Des2
- Des3 -- done

6. Encryption/ Decryption
- Encryption

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
