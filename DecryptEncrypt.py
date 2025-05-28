def encrypt(plaintext, key, version = 'DES0'):
    if len(plaintext) != 64:
        raise ValueError("Plaintext must be 64 bits")

    
    #get round keys
    round_keys = generate_round_keys(key)

    #initial permutation
    permuted = initial_perm(plaintext)

    #divide L and R
    L = permuted[:32]
    R = permuted[32:]
    
    #apply f-function
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
    ciphertext = inverse_perm(combine)
        #return ciphertext
    return ciphertext
            

def decrypt(ciphertext, key, version= 'DES0'):
    if len(ciphertext) != 64:
        raise ValueError("Ciphertext must be 64-bit long")
    #reverse the list for decryption
    round_keys = generate_round_keys(key)[::-1]
    
    #initial permutaiton
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
