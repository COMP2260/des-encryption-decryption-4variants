from DES_IMPLEMENTATION import *
from F_FUNCTION import f_function
from Key_Schedule import *
from Bit_manipulation import xor, bin2hex

def encrypt(plaintext, key, version='DES0'):
    if len(plaintext) != 64:
        raise ValueError("Plaintext must be 64 bits")

    # Store ciphertext from every round
    cipherrounds = []

    #get round keys
    round_keys = generate_round_keys(key)

    #initial permutation
    permuted = initial_perm(plaintext)

    #divide L and R
    L = permuted[:32]
    R = permuted[32:]
    
    #perform 16 Feistel rounds
    for i in range(16):
        # store pre-transformation Right Half
        old_R = R

        #apply f-function to right half
        f_func_R = f_function(R, round_keys[i], version)

        #xor with left half
        R = xor(L, f_func_R)

        #swap back with original R
        L = old_R

        # record the ciphertext after each round
        cipherrounds.append(L + R)

    #combine the final result for inverse permutaiton
    combine = R+L
    ciphertext = inverse_perm(combine)
        #return ciphertext
    return (ciphertext, cipherrounds)
            

def decrypt(ciphertext, key, version='DES0'):
    if len(ciphertext) != 64:
        raise ValueError("Ciphertext must be 64-bit long")
    #reverse the list for decryption
    round_keys = generate_round_keys(key)[::-1]
    
    #initial permutation
    permuted = initial_perm(ciphertext)

    #the rest will be implmented same with the encryption function
    L = permuted[:32]
    R = permuted[32:]

    for i in range(16):
        #swapping
        old_R = R
        #apply left function to right half
        f_func_R = f_function(R, round_keys[i], version)

        #xor with left half
        R = xor(L, f_func_R)
        #swap back with original R
        L = old_R

    #combine the final result for inverse permutaiton
    combine = R+L
    plaintext = inverse_perm(combine)
        #return ciphertext
    return plaintext

def generate_round_keys(master):
    # apply PC1 to master key
    permuted = apply_pc1(master)

    # split permuted master key into 2 halves
    C, D, splits = ["0"] * 16, ["0"] * 16, split_key(permuted)
    C[0] = splits[0]
    D[0] = splits[1]

    round_keys = list()
    for i in range(16):
        # Perform left shift on each half
        # The number of bits to shift for each round is predefined in Rotation
        C[i] = shift_left(C[i], Rotation[i])
        D[i] = shift_left(D[i], Rotation[i])

        # Join and apply PC2 transformation to the halves
        joined = C[i] + D[i]
        round_keys.append(apply_pc2(joined))

        # Prepare for next round key generation
        if (i != 15):
            C[i + 1] = C[i]
            D[i + 1] = D[i]
    
    return round_keys

def analysis_table(p1, p2, k1, k2, mode='same-key'):
    # Create a table to compare the ciphertexts after each round
    cipher1, cipher2 = [], []
    allp1rounds, allp2rounds = [], []

    if mode == 'same-key':
        output = "P and P' under K\n"
    elif mode == 'different-key':
        output = "P under K and K'\n"

    for version in ['DES0', 'DES1', 'DES2', 'DES3']:
        if mode == 'same-key':
            ciphertext_P1, p1rounds = encrypt(p1, k1, version)
            ciphertext_P2, p2rounds = encrypt(p2, k1, version)
        elif mode == 'different-key':
            ciphertext_P1, p1rounds = encrypt(p1, k1, version)
            ciphertext_P2, p2rounds = encrypt(p1, k2, version)

        # Store the ciphertexts and rounds for each version
        cipher1.append(ciphertext_P1)
        cipher2.append(ciphertext_P2)
        allp1rounds.append(p1rounds)
        allp2rounds.append(p2rounds)

    output += "Ciphertext C:\t" + cipher1[0] + f" (H: {bin2hex(cipher1[0])})" + "\n"
    output += "Ciphertext C':\t" + cipher2[0] + f" (H: {bin2hex(cipher2[0])})" + "\n"
    output += "Round\t\t\tDES0\tDES1\tDES2\tDES3\n"

    init_diff = xor(p1, p2).count('1') if mode == 'same-key' else 0     # Number of differing bits in p1 and p2
    output += f"\t0\t\t\t{init_diff}\t\t{init_diff}\t\t{init_diff}\t\t{init_diff}\n"

    # Calculate the number of differing bits in ciphertexts after each round
    for i in range(len(p1rounds)):
        output += f"\t{i+1}\t\t\t"
        for j in range(len(allp1rounds)):
            output += str(xor(allp1rounds[j][i], allp2rounds[j][i]).count('1')) + "\t\t"
        output += "\n"
    return output