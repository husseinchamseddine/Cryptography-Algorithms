from operator import xor
def generate_keys(bit_key_array):

    KL = bit_key_array[:28]
    KR = bit_key_array[28:]
    
    left_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    output = []
    for i in range(16):
        KL = KL[left_shifts[i]:] + KL[:left_shifts[i]]
        KR = KR[left_shifts[i]:] + KR[:left_shifts[i]]
        
        combined_key = KL + KR
        
        output.append(combined_key)

    return output


def initial_permutation(bits):

    initial_permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
                              60, 52, 44, 36, 28, 20, 12, 4,
                              62, 54, 46, 38, 30, 22, 14, 6,
                              64, 56, 48, 40, 32, 24, 16, 8,
                              57, 49, 41, 33, 25, 17, 9, 1,
                              59, 51, 43, 35, 27, 19, 11, 3,
                              61, 53, 45, 37, 29, 21, 13, 5,
                              63, 55, 47, 39, 31, 23, 15, 7]
    
    permuted_bits = [None] * 64
    for i, position in enumerate(initial_permutation_table):
        permuted_bits[i] = bits[position - 1]
    return permuted_bits


def hex_to_bits(hex_string):

    # Convert hexadecimal string to integer
    integer_value = int(hex_string, 16)
    
    # Convert integer to binary string
    binary_string = bin(integer_value)[2:]
    
    # Pad binary string with leading zeros to ensure it's 64 bits long
    binary_string = binary_string.zfill(64)
    
    return binary_string

def bits_to_hex(bits_array):
    hex_string = ""
    for i in range(0, len(bits_array), 4):
        hex_digit = ""
        for j in range(4):
            hex_digit += str(bits_array[i+j])
        hex_string += hex(int(hex_digit, 2))[2:] #[2:] to remove the 0x
    return hex_string

def key_permutation_56(key_array):

    key_permutation_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 
        19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4
    ]
    key_56_bits = [None] * 56
    for i, position in enumerate(key_permutation_table):
        key_56_bits[i] = key_array[position - 1]
    return key_56_bits

def key_permutation_48(key_array):
    key_permutation_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]

    permuted_key = [None] * 48
    for i, position in enumerate(key_permutation_table):
        permuted_key[i] = key_array[position - 1]
    
    return permuted_key

def S_box(key_array):
    S_boxes = [
        #Sbox1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        #Sbox2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        #Sbox3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        #Sbox4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        #Sbox5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        #Sbox6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        #Sbox7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        #Sbox8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    output_bits = []
    for i in range(8):
        
        s_box_input = key_array[i*6 : (i+1)*6]
        row = 2 * s_box_input[0] + s_box_input[5]
        column = 8 * s_box_input[1] + 4 * s_box_input[2] + 2 * s_box_input[3] + s_box_input[4]
        value = S_boxes[i][row][column]
        # Convert the decimal value to binary string
        binary_value = bin(value)[2:].zfill(4)
        # Append the binary digits to the output_bits list
        output_bits.extend([int(bit) for bit in binary_value])

    return output_bits

def expansion(array_bit):
    expansion_table = [
        32,  1,  2,  3,  4,  5,
         4,  5,  6,  7,  8,  9,
         8,  9,  10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32,  1
    ]

    expanded_array = [array_bit[i-1] for i in expansion_table]

    return expanded_array

def permute_32(bit_array):
    permutation_table = [
        16,  7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26,  5, 18, 31,  10,
         2,  8, 24, 14, 32, 27,  3,  9,
        19, 13, 30,  6, 22, 11,  4, 25
    ]
    permuted_array = [bit_array[i-1] for i in permutation_table]

    return permuted_array


def inverse_initial_permutation(array_bits):
    inverse_initial_permutation_table = [
        40,  8, 48, 16, 56, 24, 64, 32,
        39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25
    ]

    permuted_bits = [None] * 64
    for i, position in enumerate(inverse_initial_permutation_table):
        permuted_bits[i] = array_bits[position - 1]
    return permuted_bits

def encrypt(message, key):
    
    if len(message) != 16:
        return "Error, the plaintext must be of size 64 bits"
    
    bit_message = hex_to_bits(message)
    # the message in binary is:  1111000100110100111111111111101010111100110101010100011011111100

    bit_key = hex_to_bits(key)
    #the key in binary is:  0010001000100010001100110011001101000100010001000101010101010101

    bit_message_array = [int(i) for i in bit_message]
    bit_key_array = [int(i) for i in bit_key]

    IP = initial_permutation(bit_message_array)
    #Initial permutation of message:  [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
   
    # Slice bitMessage into left and right halves
    LE0 = IP[:32]
    #L0 of message:  edbff625

    RE0 = IP[32:]
    #R0 of message:  bd9f9c4c

    K = key_permutation_56(bit_key_array)
    #The initial permutation of the key is:  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

    L = generate_keys(K)
    #L is an array that contains all the keys of the 16 rounds 

    for i in range(1, 17):
       
        K = L[i-1]
        #Key left shifted 1 is:  01e01f81fe0018

        K_i_48 = key_permutation_48(K)
        #Key of round 1 is:  3038445022c5


        R_i_expanded = expansion(RE0)
        #R0 expanded is:  5fbcffcf8259

        F_out = [xor(R_i_expanded[i], K_i_48[i]) for i in range(48)]
        #Feistal output of round 1 is:  6f84bb9fa09c


        Sbox_out = S_box(F_out)
        #Sbox output of round 1 is:  59d77dbc


        permuted_R_i = permute_32(Sbox_out)
        #Permutation output of R round 1 is:  be4df5ab

       

        R_out = [xor(permuted_R_i[i], LE0[i]) for i in range(32)]
        #R xor L output of round 1 is:  53f2038e


        LE0 = RE0
        #L1= bd9f9c4c


        RE0 = R_out 
        #R1= 53f2038e


    temp = LE0
    LE0 = RE0
    RE0 = temp
    #Last 32 bit swap
    cipher_before_IP=LE0+RE0
    cipher_bits = inverse_initial_permutation(cipher_before_IP)
    cipher_text = bits_to_hex(cipher_bits)
  
    steps = []
    

    
    steps.append(f"The message in binary is: {bit_message}")
    # Append all other steps similarly

    steps.append(f"The key in binary is: {bit_key}")

    steps.append(f"The initial permutation of the message is: {IP}")

    steps.append(f"L0 of message: {LE0}")

    steps.append(f"RE of message: {RE0}")

    steps.append(f"The initial permutation of the key is: {K}")    



    steps.append("############################# Rounds will start now #############################")

    for i in range(1, 17):
        # ... perform the round operations ...

        # Append the round-specific steps to the steps list
        steps.append(f"Key left shifted {i} is: {bits_to_hex(L[i-1])}")
        steps.append(f"Key of round {i} is: {bits_to_hex(K_i_48)}")
        steps.append(f"R{i-1} expanded is: {bits_to_hex(R_i_expanded)}")
        steps.append(f"Feistal output of round {i} is: {bits_to_hex(F_out)}")
        steps.append(f"Sbox output of round {i} is: {bits_to_hex(Sbox_out)}")
        steps.append(f"Permutation output of R round {i} is: {bits_to_hex(permuted_R_i)}")
        steps.append(f"R xor L output of round {i} is: {bits_to_hex(R_out)}")
        steps.append(f"L{i}= {bits_to_hex(LE0)}")
        steps.append(f"R{i}= {bits_to_hex(RE0)}")
        steps.append(f"############################# Round {i} Done #############################")

    return cipher_text, steps


def decrypt(message,key):
    bit_message = hex_to_bits(message)
    bit_key = hex_to_bits(key)

    bit_message_array = [int(i) for i in bit_message]
    bit_key_array = [int(i) for i in bit_key]
    IP = initial_permutation(bit_message_array)

    # Slice bitMessage into left and right halves
    LE0 = IP[:32]

    RE0 = IP[32:]

    K = key_permutation_56(bit_key_array)

    L = generate_keys(K)

    for i in range(1, 17):
        
        K = L[16-i]


        K_i_48 = key_permutation_48(K)
  
        R_i_expanded = expansion(RE0)


        F_out = [xor(R_i_expanded[i], K_i_48[i]) for i in range(48)]
      

        Sbox_out = S_box(F_out)
        

        permuted_R_i = permute_32(Sbox_out)
       

        R_out = [xor(permuted_R_i[i], LE0[i]) for i in range(32)]
        

        LE0 = RE0
        RE0 = R_out 
        
    
    temp = LE0
    LE0 = RE0
    RE0 = temp
    cipher_before_IP=LE0+RE0
    cipher_bits = inverse_initial_permutation(cipher_before_IP)
    plaintext = bits_to_hex(cipher_bits)

    steps = []

    steps.append(f"The message in binary is: {bit_message}")
    # Append all other steps similarly

    steps.append(f"The key in binary is: {bit_key}")

    steps.append(f"The initial permutation of the message is: {IP}")

    steps.append(f"L0 of message: {LE0}")

    steps.append(f"RE of message: {RE0}")

    steps.append(f"The initial permutation of the key is: {K}")    



    steps.append("############################# Rounds will start now #############################")

    for i in range(1, 17):
        # ... perform the round operations ...

        # Append the round-specific steps to the steps list
        steps.append(f"Key left shifted {i} is: {bits_to_hex(L[i-1])}")
        steps.append(f"Key of round {i} is: {bits_to_hex(K_i_48)}")
        steps.append(f"R{i-1} expanded is: {bits_to_hex(R_i_expanded)}")
        steps.append(f"Feistal output of round {i} is: {bits_to_hex(F_out)}")
        steps.append(f"Sbox output of round {i} is: {bits_to_hex(Sbox_out)}")
        steps.append(f"Permutation output of R round {i} is: {bits_to_hex(permuted_R_i)}")
        steps.append(f"R xor L output of round {i} is: {bits_to_hex(R_out)}")
        steps.append(f"L{i}= {bits_to_hex(LE0)}")
        steps.append(f"R{i}= {bits_to_hex(RE0)}")
        steps.append(f"############################# Round {i} Done #############################")

    return plaintext, steps


